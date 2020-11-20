[TOC]

## Spring 开发

Spring 是一个支持快速开发 Java EE 应用程序的框架。它提供了一系列底层容器和基础设施，并可以和大量常用的开源框架无缝集成，可以说是 Java EE 应用程序的必备。

随着 Spring 越来越受欢迎，在 Spring Framework 基础上，又诞生了 Spring Boot、Spring Cloud、Spring Data、Spring Security 等一系列基于 Spring Framework 的项目。

### Ioc 容器

#### IoC 原理

**容器**是一种为某种特定组件的运行提供必要支持的一个软件环境。例如，Tomcat 就是一个 Servlet 容器，它可以为 Servlet 的运行提供运行环境。类似 Docker 这样的软件也是一个容器，它提供了必要的 Linux 环境以便运行一个特定的 Linux 进程。

通常来说，使用容器运行组件，除了提供一个组件运行环境之外，容器还提供了许多底层服务。

Spring 的核心就是提供了一个 IoC 容器，它可以管理所有轻量级的 JavaBean 组件，提供的底层服务包括组件的生命周期管理、配置和组装服务、AOP 支持，以及建立在 AOP 基础上的声明式事务服务等。

**IoC** 全称 **Inversion of Control**，直译为**控制反转**。

1. 通过 `BookService` 获取书籍：

   `BookService` --> 需要持有一个 `DataSource` instance --> 为了实例化一个 `DataSource` instance 又需要实例化一个 `Config` instance。

2. 通过 `UserService` 获取用户：

   `UserService` --> 需要持有一个 `DataSource` instance --> 为了实例化一个 `DataSource` instance 又需要实例化一个 `Config` instance。

3. 在处理用户购买的 `CartServlet` 中，需要实例化 `UserService` and `BookService` --> 那么 `UserService` 和 `BookService` 又分别需要实例化 `DataSource`，进而又需要实例化 `Config`。

4. 上述这种方式的缺点：

   1. 每个组件都采用一种简单的 `new` 创建实例并持有。
   2. 实例化一个组件可能很困难，比如为了创建 `BookService` or `UserService` 需要创建 `DataSource`，进而又需要创建 `Config`。
   3. 没有必要让 `BookService` 和 `UserService` 分别创建 `DataSource` 实例，完全可以共享一个 `DataSource`。但是谁负责创建和管理 `DataSource` 实例又显得很困难。
   4. 随着组件的增多，组件的共享和相互之间的依赖关系就变得困难。

5. 基于上述方式的缺点，需要考虑的核心问题有：

   1. 谁负责创建组件？
   2. 谁负责根据依赖关系组装组件？
   3. 销毁时，如何根据依赖关系正确销毁？

6. 解决上述核心问题的核心方案就是 **IoC**：

   1. 在传统的应用程序中，控制权在程序本身，程序的流程控制完全有开发者控制。这种模式的缺点是，一个组件如果要使用另一个组件，必须先知道如何正确地创建它。

   2. 在IoC模式下，控制权发生了反转，即从应用程序转移到了IoC容器，所有组件不再由应用程序自己创建和配置，而是由IoC容器负责，这样，应用程序只需要直接使用已经创建好并且配置好的组件。为了能让组件在IoC容器中被“装配”出来，需要某种“注入”机制，例如，`BookService`自己并不会创建`DataSource`，而是等待外部通过`setDataSource()`方法来注入一个`DataSource`，不直接`new`一个`DataSource`，而是注入一个`DataSource`，这个小小的改动虽然简单，却带来了一系列好处：

      1. `BookService` 不再关心如何创建 `DataSource`，因此，不必编写读取数据库配置之类的代码；
      2. `DataSource` 实例被注入到 `BookService`，同样也可以注入到 `UserService`，因此，**共享**一个组件非常简单；
      3. 测试 `BookService` 更容易，因为注入的是 `DataSource`，可以使用内存数据库，而不是真实的MySQL配置。

      ```java
      public class BookService {
          private DataSource dataSource;
      
          public void setDataSource(DataSource dataSource) {	// 通过 `setDataSource()` 方法注入一个 `DataSource`，而不是直接 `new` 一个 `DataSource`
              this.dataSource = dataSource;
          }
      }
      ```

   3. **IoC** 又称为依赖注入(**DI：Dependency Injection**)，它解决了一个最主要的问题：将组件的创建+配置与组件的使用相分离，并且，由 IoC 容器负责管理组件的生命周期。

      因为 IoC 容器要负责实例化所有的组件，因此，有必要告诉容器如何创建组件，以及各组件的依赖关系。一种最简单的配置是通过 XML 文件来实现:

      ```xml
      <beans>
          <bean id="dataSource" class="HikariDataSource" />
          <bean id="bookService" class="BookService">
              <property name="dataSource" ref="dataSource" />
          </bean>
          <bean id="userService" class="UserService">
              <property name="dataSource" ref="dataSource" />
          </bean>
      </beans>
      ```

7. 依赖注入方式

   1. 依赖注入可以通过 `set()` 方法实现：

      ```java
      public class BookService {
          private DataSource dataSource;
      
          public void setDataSource(DataSource dataSource) {	// 通过 `setDataSource()` 方法注入一个 `DataSource`，而不是直接 `new` 一个 `DataSource`
              this.dataSource = dataSource;
          }
      }
      ```

   2. 依赖注入也可以通过构造方法实现。

      ```java
      public class BookService {
          private DataSource dataSource;
      
          public BookService(DataSource dataSource) {
              this.dataSource = dataSource;
          }
      }
      ```

   3. Spring 的 IoC 容器同时支持属性注入和构造方法注入，并允许混合使用。

8. 无侵入容器

   在设计上，Spring 的 IoC 容器是一个高度可扩展的无侵入容器。**所谓无侵入，是指应用程序的组件无需实现Spring的特定接口**，或者说，组件根本不知道自己在Spring的容器中运行。这种无侵入的设计有以下好处：

   1. 应用程序组件既可以在Spring的IoC容器中运行，也可以自己编写代码自行组装配置；
   2. 测试的时候并不依赖Spring容器，可单独进行测试，大大提高了开发效率。



#### 装配 Bean

到底如何使用 IoC 容器？装配好的 Bean 又如何使用？

1. 首先，通过 Maven 创建工程并引入 `spring-context` 依赖：

   ```xml
   <project xmlns="http://maven.apache.org/POM/4.0.0"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
       <modelVersion>4.0.0</modelVersion>
   
       <groupId>com.itranswarp.learnjava</groupId>
       <artifactId>spring-ioc-appcontext</artifactId>
       <version>1.0-SNAPSHOT</version>
       <packaging>jar</packaging>
   
       <properties>
           <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
           <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
           <maven.compiler.source>11</maven.compiler.source>
           <maven.compiler.target>11</maven.compiler.target>
           <java.version>11</java.version>
   
           <spring.version>5.2.3.RELEASE</spring.version>
       </properties>
   
       <dependencies>
           <dependency>
               <groupId>org.springframework</groupId>
               <artifactId>spring-context</artifactId>
               <version>${spring.version}</version>
           </dependency>
       </dependencies>
   </project>
   ```

2. 例子

   1. 编写 `MailService`，用于用户注册或登录成功后发送邮件通知，包含方法：

      * `public void sendRegistrationMail(User user)`
      * `public void sendLoginMail(User user)`

   2. 编写 `UserService`，用于实现用户注册和登录，包含主要方法：

      * `public void setMailService(MailService mailService)`，用于注入 `MailService`
      * `public User login(String email, String password)`
      * `public User register(String email, String password, String name)`

   3. 编写一个特定的 `application.xml` 配置文件，告诉 Spring 的 IoC 容器应该如何创建并组装 Bean：

      ```xml
      <?xml version="1.0" encoding="UTF-8"?>
      <beans xmlns="http://www.springframework.org/schema/beans"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://www.springframework.org/schema/beans
              https://www.springframework.org/schema/beans/spring-beans.xsd">
      
          <bean id="userService" class="com.itranswarp.learnjava.service.UserService">
              <property name="mailService" ref="mailService" />
          </bean>
      
          <bean id="mailService" class="com.itranswarp.learnjava.service.MailService" />
      </beans>
      ```

      * 每个`<bean ...>` 都有一个`id`标识，相当于Bean的唯一ID；
      * 在`userService` Bean中，通过`<property name="..." ref="..." />`注入了另一个Bean；
      * Bean的顺序不重要，Spring根据依赖关系会自动正确初始化。

   4. 最后一步，我们需要创建一个 Spring 的 IoC 容器实例，然后加载配置文件，让 Spring 容器为我们创建并装配好配置文件中指定的所有 Bean，这只需要一行代码：

      ```java
      ApplicationContext context = new ClassPathXmlApplicationContext("application.xml");
      ```

   5. 接下来，我们就可以从Spring容器中“取出”装配好的Bean然后使用它：

      ```java
      // 获取Bean:
      UserService userService = context.getBean(UserService.class);
      // 正常调用:
      User user = userService.login("bob@example.com", "password");
      ```

      完整的 `main()` 方法如下：

      ``` java
      public class Main {
          public static void main(String[] args) {
              ApplicationContext context = new ClassPathXmlApplicationContext("application.xml");
              UserService userService = context.getBean(UserService.class);
              User user = userService.login("bob@example.com", "password");
              System.out.println(user.getName());
          }
      }
      ```

      * **ApplicationContext:** Spring 容器就是`ApplicationContext`，它是一个接口，有很多实现类，这里我们选择 `ClassPathXmlApplicationContext`，表示它会自动从 classpath 中查找指定的 XML 配置文件。

        ```java
        ApplicationContext context = new ClassPathXmlApplicationContext("application.xml");
        ```

      * 获得了`ApplicationContext`的实例，就获得了IoC容器的引用。从`ApplicationContext`中我们可以根据Bean的ID获取Bean，但更多的时候我们根据Bean的类型获取Bean的引用：

        ```java
        UserService userService = context.getBean(UserService.class);
        ```

   6. Spring 还提供了另一种 IoC 容器叫 `BeanFactory`，使用方法和 `ApplicationContext` 类似：

      ```java
      BeanFactory factory = new XmlBeanFactory(new ClassPathResource("application.xml"));
      MailService mailService = factory.getBean(MailService.class);
      ```

      * `BeanFactory`和`ApplicationContext`的区别在于，`BeanFactory`的实现是按需创建，即第一次获取Bean时才创建这个Bean，而`ApplicationContext`会一次性创建所有的Bean。
      * 实际上，`ApplicationContext`接口是从`BeanFactory`接口继承而来的，并且，`ApplicationContext`提供了一些额外的功能，包括国际化支持、事件和通知机制等。
      * 通常情况下，我们总是使用`ApplicationContext`，很少会考虑使用`BeanFactory`。

3. 小结

   1. Spring的IoC容器接口是`ApplicationContext`，并提供了多种实现类；
   2. 通过XML配置文件创建IoC容器时，使用`ClassPathXmlApplicationContext`；
   3. 持有IoC容器后，通过`getBean()`方法获取Bean的引用。

   

#### 使用 Annotation(注解) 配置

使用Spring的IoC容器，实际上就是**通过类似XML这样的配置文件**，把我们自己的Bean的依赖关系描述出来，然后让容器来创建并装配Bean。一旦容器初始化完毕，我们就直接从容器中获取Bean使用它们。

使用XML配置的优点是所有的Bean都能一目了然地列出来，并通过配置注入能直观地看到每个Bean的依赖。它的缺点是写起来非常繁琐，每增加一个组件，就必须把新的Bean配置到XML中。

有没有其他更简单的配置方式呢？

有！我们可以使用Annotation配置，可以完全不需要XML，让Spring自动扫描Bean并组装它们。

1. 首先，给 `MailService` 添加 `@Component` 注解：

   ```java
   @Component
   public class MailService {
       ...
   }
   ```

   * 这个 `@Component` 注解就相当于定义了一个Bean，它有一个可选的名称，默认是 `mailService`，即小写开头的类名。

2. 然后给 `UserService` 添加 `@Component` 注解和一个 `@Autowired` 注解：

   ```java
   @Component
   public class UserService {
       @Autowired
       MailService mailService;
   
       ...
   }
   ```

   * `@Component` 注解就相当于定义了一个Bean

   * 使用`@Autowired`就相当于把指定类型的Bean注入到指定的字段中。也就是，将 `MailService` 类型的 Bean 注入到 `mailService` 中。和XML配置相比，`@Autowired`大幅简化了注入，因为它不但可以写在`set()`方法上，还可以直接写在字段上，甚至可以写在构造方法中：

     ```java
     @Component
     public class UserService {
         MailService mailService;
     
         public UserService(@Autowired MailService mailService) {
             this.mailService = mailService;
         }
         ...
     }
     ```

   * 我们一般把`@Autowired`写在字段上，通常使用package权限的字段，便于测试。

3. 最后，编写 `AppConfig` 类启动容器：

   ```java
   @Configuration
   @ComponentScan
   public class AppConfig {
       public static void main(String[] args) {
           ApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);
           UserService userService = context.getBean(UserService.class);
           User user = userService.login("bob@example.com", "password");
           System.out.println(user.getName());
       }
   }
   ```

   * 除了`main()`方法外，`AppConfig`标注了`@Configuration`，表示它是一个配置类，因为我们创建`ApplicationContext`时，使用的实现类是`AnnotationConfigApplicationContext`，必须传入一个标注了`@Configuration`的类名。
   * 此外，`AppConfig`还标注了`@ComponentScan`，它告诉容器，自动搜索当前类所在的包以及子包，把所有标注为`@Component`的Bean自动创建出来，并根据`@Autowired`进行装配。

4. 使用Annotation配合自动扫描能大幅简化Spring的配置，我们只需要保证：

   - 每个Bean被标注为`@Component`并正确使用`@Autowired`注入；
   - 配置类被标注为`@Configuration`和`@ComponentScan`；
   - 所有Bean均在指定包以及子包内。

   使用`@ComponentScan`非常方便，但是，我们也要特别注意包的层次结构。通常来说，启动配置`AppConfig`位于自定义的顶层包（例如`com.itranswarp.learnjava`），其他Bean按类别放入子包。

5. 小结

   1. 使用Annotation可以大幅简化配置，每个Bean通过`@Component`和`@Autowired`注入；
   2. 必须合理设计包的层次结构，才能发挥`@ComponentScan`的威力。



#### 定制 Bean

1. **Scope：**

   1. **Singleton:** 对于Spring容器来说，当我们把一个Bean标记为`@Component`后，它就会自动为我们创建一个单例（Singleton），即容器初始化时创建Bean，容器关闭前销毁Bean。在容器运行期间，我们调用`getBean(Class)`获取到的Bean总是同一个实例。

   2. **Prototype:** 还有一种Bean，我们每次调用`getBean(Class)`，容器都返回一个**新的实例**，这种Bean称为Prototype（原型），它的生命周期显然和Singleton不同。声明一个Prototype的Bean时，需要添加一个额外的`@Scope`注解：

      ```java
      @Component
      @Scope(ConfigurableBeanFactory.SCOPE_PROTOTYPE) // @Scope("prototype")
      public class MailSession {
          ...
      }
      ```

2. 注入 List

   有些时候，我们会有一系列接口相同，不同实现类的Bean。例如，注册用户时，我们要对email、password和name这3个变量进行验证。

   1. 首先定义验证接口 `Validator`:

      ```java
      public interface Validator {	// This is an interface
          void validate(String email, String password, String name);
      }
      ```

      创建 interface `Validator`。

   2. 然后，分别使用 3 个 `Validator` 对用户参数进行验证：

      ```java
      @Component
      public class EmailValidator implements Validator {
          public void validate(String email, String password, String name) {
              if (!email.matches("^[a-z0-9]+\\@[a-z0-9]+\\.[a-z]{2,10}$")) {
                  throw new IllegalArgumentException("invalid email: " + email);
              }
          }
      }
      
      @Component
      public class PasswordValidator implements Validator {
          public void validate(String email, String password, String name) {
              if (!password.matches("^.{6,20}$")) {
                  throw new IllegalArgumentException("invalid password");
              }
          }
      }
      
      @Component
      public class NameValidator implements Validator {
          public void validate(String email, String password, String name) {
              if (name == null || name.isBlank() || name.length() > 20) {
                  throw new IllegalArgumentException("invalid name: " + name);
              }
          }
      }
      ```

      * 创建的 3 个 Bean，`EmailValidator`, `PasswordValidator`, `NameValidator`，这三个 Bean 都实现了相同的 interface `Validator`。

   3. 最后，我们通过一个`Validators`作为入口进行验证：

      ```java
      @Component
      public class Validators {
          @Autowired
          List<Validator> validators;	// 向 class Validators 注入 List<Validator>
      
          public void validate(String email, String password, String name) {
              for (var validator : this.validators) {
                  validator.validate(email, password, name);
              }
          }
      }
      ```

      * 注意到 class `Validators` 别注入了一个 `List<Validator>`，Spring 会自动把所有类型为 `Validator` 的 Bean 装配为一个 `List`，然后注入进来。这样一来，每新增一个 `Validator` 类型，就会被 Spring 装配到 `Validators` 中，非常方便。

      * 因为Spring是通过扫描classpath获取到所有的Bean，而`List`是有序的，要指定`List`中Bean的顺序，可以加上`@Order`注解：

        ```java
        @Component
        @Order(1)
        public class EmailValidator implements Validator {
            ...
        }
        
        @Component
        @Order(2)
        public class PasswordValidator implements Validator {
            ...
        }
        
        @Component
        @Order(3)
        public class NameValidator implements Validator {
            ...
        }
        ```

3. 可选注入

   * 默认情况下，当我们标记了一个`@Autowired`后，Spring如果没有找到对应类型的Bean，它会抛出`NoSuchBeanDefinitionException`异常。

   * 可以给`@Autowired`增加一个`required = false`的参数。这个参数告诉Spring容器，如果找到一个类型为`ZoneId`的Bean，就注入，如果找不到，就忽略。这种方式非常适合有定义就使用定义，没有就使用默认值的情况。

     ```java
     @Component
     public class MailService {
         @Autowired(required = false)
         ZoneId zoneId = ZoneId.systemDefault();
         ...
     }
     ```

4. 创建第三方 Bean

   如果一个Bean不在我们自己的package管理之内，例如`ZoneId`，如何创建它？答案是**我们自己在`@Configuration`类中编写一个Java方法创建并返回它，注意给方法标记一个`@Bean`注解**，Spring对标记为`@Bean`的方法只调用一次，因此返回的Bean仍然是单例。

   ```java
   @Configuration
   @ComponentScan
   public class AppConfig {
       // 创建一个Bean:
       @Bean
       ZoneId createZoneId() {
           return ZoneId.of("Z");
       }
   }
   ```

   

5. 初始化和销毁

   有些时候，一个 Bean 在注入必要的依赖后，需要进行**初始化**（监听消息等）。在容器关闭时，有时候还需要**清理资源**（关闭连接池等）。我们通常会定义一个 `init()` 方法进行初始化，定义一个 `shutdown()` 方法进行清理，然后，引入 JSR-250 定义的 Annotation。

   在 Bean 的初始化和清理方法上标记 `@PostConstruct` and `@PreDestrory`: 

   ```java
   @Component
   public class MailService {
       @Autowired(required = false)
       ZoneId zoneId = ZoneId.systemDefault();
   
       @PostConstruct
       public void init() {
           System.out.println("Init mail service with zoneId = " + this.zoneId);
       }
   
       @PreDestroy
       public void shutdown() {
           System.out.println("Shutdown mail service");
       }
   }
   ```

   Spring容器会对上述Bean做如下初始化流程：

   - 调用构造方法创建`MailService`实例；
   - 根据`@Autowired`进行注入；
   - 调用标记有`@PostConstruct`的`init()`方法进行初始化。
   - 而销毁时，容器会首先调用标记有`@PreDestroy`的`shutdown()`方法。

   **???***  Spring只根据Annotation查找无参数方法，对方法名不作要求。*

6. 使用别名

   1. 默认情况下，对一种类型的Bean，容器只创建一个实例。但有些时候，我们需要对一种类型的Bean创建多个实例。例如，同时连接多个数据库，就必须创建多个`DataSource`实例。

      如果我们在`@Configuration`类中创建了多个同类型的Bean，Spring会报`NoUniqueBeanDefinitionException`异常，意思是出现了重复的Bean定义。

      ```java
      @Configuration
      @ComponentScan
      public class AppConfig {
          @Bean
          ZoneId createZoneOfZ() {
              return ZoneId.of("Z");
          }
      
          @Bean
          ZoneId createZoneOfUTC8() {
              return ZoneId.of("UTC+08:00");
          }
      }	
      ```

   2. 这个时候，需要给每个Bean添加不同的名字：

      ```java
      @Configuration
      @ComponentScan
      public class AppConfig {
          @Bean("z")
          ZoneId createZoneOfZ() {
              return ZoneId.of("Z");
          }
      
          @Bean
          @Qualifier("utc8")
          ZoneId createZoneOfUTC8() {
              return ZoneId.of("UTC+08:00");
          }
      }
      ```

      * 可以用`@Bean("name")`指定别名，也可以用`@Bean`+`@Qualifier("name")`指定别名。

   3. 存在多个同类型的Bean时，注入`ZoneId`又会报错。

      ```java
      NoUniqueBeanDefinitionException: No qualifying bean of type 'java.time.ZoneId' available: expected single matching bean but found 2
      ```

      意思是期待找到唯一的 `ZoneId` 类型 Bean，但是找到两个。因此，注入时，要指定Bean的名称：

      ```java
      @Component
      public class MailService {
      	@Autowired(required = false)
      	@Qualifier("z") // 指定注入名称为"z"的ZoneId
      	ZoneId zoneId = ZoneId.systemDefault();
          ...
      }
      ```

      * 指定注入名称为 **"z"** 的ZoneId。

   4. 还有一种方法是把其中某个Bean指定为`@Primary`，这样，在注入时，如果没有指出Bean的名字，Spring会注入标记有`@Primary`的Bean。

      ```java
      @Configuration
      @ComponentScan
      public class AppConfig {
          @Bean
          @Primary // 指定为主要Bean
          @Qualifier("z")
          ZoneId createZoneOfZ() {
              return ZoneId.of("Z");
          }
      
          @Bean
          @Qualifier("utc8")
          ZoneId createZoneOfUTC8() {
              return ZoneId.of("UTC+08:00");
          }
      }
      ```

      这种方式也很常用。例如，对于主从两个数据源，通常将主数据源定义为`@Primary`：

      ```java
      @Configuration
      @ComponentScan
      public class AppConfig {
          @Bean
          @Primary
          DataSource createMasterDataSource() {
              ...
          }
      
          @Bean
          @Qualifier("slave")
          DataSource createSlaveDataSource() {
              ...
          }
      }
      ```

      * 其他Bean默认注入的就是主数据源。如果要注入从数据源，那么只需要指定名称即可。

7. 使用 FactoryBean

   我们在设计模式的[工厂方法](https://www.liaoxuefeng.com/wiki/1252599548343744/1281319170474017)中讲到，很多时候，可以通过工厂模式创建对象。Spring也提供了工厂模式，允许定义一个工厂，然后由工厂创建真正的Bean。

   用工厂模式创建Bean需要实现`FactoryBean`接口。我们观察下面的代码：

   ```java
   @Component
   public class ZoneIdFactoryBean implements FactoryBean<ZoneId> {
   
       String zone = "Z";
   
       @Override
       public ZoneId getObject() throws Exception {
           return ZoneId.of(zone);
       }
   
       @Override
       public Class<?> getObjectType() {
           return ZoneId.class;
       }
   }
   ```

   * 当一个Bean实现了`FactoryBean`接口后，Spring会先实例化这个工厂，然后调用`getObject()`创建真正的Bean。
   * `getObjectType()`可以指定创建的Bean的类型，因为指定类型不一定与实际类型一致，可以是接口或抽象类。
   * 因此，如果定义了一个`FactoryBean`，要注意Spring创建的Bean实际上是这个`FactoryBean`的`getObject()`方法返回的Bean。
   * 为了和普通Bean区分，我们通常都以`XxxFactoryBean`命名。

8. 小结

   * Spring默认使用Singleton创建Bean，也可指定Scope为Prototype；
   * 可将相同类型的Bean注入`List`；
   * 可用`@Autowired(required=false)`允许可选注入；
   * 可用带`@Bean`标注的方法创建Bean；
   * 可使用`@PostConstruct`和`@PreDestroy`对Bean进行初始化和清理；
   * 相同类型的Bean只能有一个指定为`@Primary`，其他必须用`@Quanlifier("beanName")`指定别名；
   * 注入时，可通过别名`@Quanlifier("beanName")`指定某个Bean；
   * 可以定义`FactoryBean`来使用工厂模式创建Bean。

#### 使用 Resource

1. 在Java程序中，我们经常会读取配置文件、资源文件等。使用Spring容器时，我们也可以把“文件”注入进来，方便程序读取。Spring提供了一个`org.springframework.core.io.Resource`（注意不是`javax.annotation.Resource`），它可以像`String`、`int`一样使用`@Value`注入：

    ```java
    @Component
    public class AppService {
        @Value("classpath:/logo.txt")
        private Resource resource;

        private String logo;

        @PostConstruct
        public void init() throws IOException {
            try (var reader = new BufferedReader(
                    new InputStreamReader(resource.getInputStream(), StandardCharsets.UTF_8))) {
                this.logo = reader.lines().collect(Collectors.joining("\n"));
            }
        }
    }
    ```

2. 注入`Resource`最常用的方式是通过classpath，即类似`classpath:/logo.txt`表示在classpath中搜索`logo.txt`文件，然后，我们直接调用`Resource.getInputStream()`就可以获取到输入流，避免了自己搜索文件的代码。

    也可以直接指定文件的路径，例如：
    ```
    @Value("file:/path/to/logo.txt")
    private Resource resource;
    ```

3. 但使用classpath是最简单的方式。上述工程结构如下：

    ```ascii
    spring-ioc-resource
    ├── pom.xml
    └── src
        └── main
            ├── java
            │   └── com
            │       └── itranswarp
            │           └── learnjava
            │               ├── AppConfig.java
            │               └── AppService.java
            └── resources
                └── logo.txt
    ```

    使用Maven的标准目录结构，所有资源文件放入`src/main/resources`即可。
    
4. 小结

    * Spring提供了Resource类便于注入资源文件。最常用的注入是通过classpath以`classpath:/path/to/file`的形式注入。

#### 注入配置

1. 在开发应用程序时，经常需要读取配置文件。最常用的配置方法是以`key=value`的形式写在`.properties`文件中。

2. 要读取配置文件，我们可以使用上一节讲到的`Resource`来读取位于classpath下的一个`app.properties`文件。但是，这样仍然比较繁琐。

3. Spring容器还提供了一个更简单的`@PropertySource`来自动读取配置文件。我们只需要在`@Configuration`配置类上再添加一个注解：

   ```java
   @Configuration
   @ComponentScan
   @PropertySource("app.properties") // 表示读取classpath的app.properties
   public class AppConfig {
       @Value("${app.zone:Z}")
       String zoneId;
   
       @Bean
       ZoneId createZoneId() {
           return ZoneId.of(zoneId);
       }
   }
   ```

   * Spring容器看到`@PropertySource("app.properties")`注解后，自动读取这个配置文件，然后，我们使用`@Value`正常注入。

   * 注意注入的字符串语法，它的格式如下：

     - `"${app.zone}"`表示读取key为`app.zone`的value，如果key不存在，启动将报错；
     - `"${app.zone:Z}"`表示读取key为`app.zone`的value，但如果key不存在，就使用默认值`Z`。

     这样一来，我们就可以根据`app.zone`的配置来创建`ZoneId`。

   * 还可以把注入的注解写到方法参数中：

     ```java
     @Bean
     ZoneId createZoneId(@Value("${app.zone:Z}") String zoneId) {
         return ZoneId.of(zoneId);
     }
     ```

   * 可见，先使用`@PropertySource`读取配置文件，然后通过`@Value`以`${key:defaultValue}`的形式注入，可以极大地简化读取配置的麻烦。

4. 另一种注入配置的方式是先通过一个简单的JavaBean持有所有的配置，例如，一个`SmtpConfig`：

   ```java
   @Component
   public class SmtpConfig {
       @Value("${smtp.host}")
       private String host;
   
       @Value("${smtp.port:25}")
       private int port;
   
       public String getHost() {
           return host;
       }
   
       public int getPort() {
           return port;
       }
   }
   ```

   然后，在需要读取的地方，使用`#{smtpConfig.host}`注入：

   ```java
   @Component
   public class MailService {
       @Value("#{smtpConfig.host}")
       private String smtpHost;
   
       @Value("#{smtpConfig.port}")
       private int smtpPort;
   }
   ```

   * 注意观察`#{}`这种注入语法，它和`${key}`不同的是，`#{}`表示从JavaBean读取属性。`"#{smtpConfig.host}"`的意思是，从名称为`smtpConfig`的Bean读取`host`属性，即调用`getHost()`方法。
   * 一个Class名为`SmtpConfig`的Bean，它在Spring容器中的默认名称就是`smtpConfig`，除非用`@Qualifier`指定了名称。

5. 小结

   Spring容器可以通过`@PropertySource`自动读取配置，并以`@Value("${key}")`的形式注入；

   可以通过`${key:defaultValue}`指定默认值；

   以`#{bean.property}`形式注入时，Spring容器自动把指定Bean的指定属性值注入。

#### 使用条件装配

开发应用程序时，我们会使用开发环境，例如，使用内存数据库以便快速启动。而运行在生产环境时，我们会使用生产环境，例如，使用MySQL数据库。如果应用程序可以根据自身的环境做一些适配，无疑会更加灵活。

Spring为应用程序准备了Profile这一概念，用来表示不同的环境。例如，我们分别定义开发、测试和生产这3个环境：
* native
* test
* production

1. 创建某个Bean时，Spring容器可以根据注解`@Profile`来决定是否创建。例如，以下配置：

   ```java
   @Configuration
   @ComponentScan
   public class AppConfig {
       @Bean
       @Profile("!test")
       ZoneId createZoneId() {
           return ZoneId.systemDefault();
       }
   
       @Bean
       @Profile("test")
       ZoneId createZoneIdForTest() {
           return ZoneId.of("America/New_York");
       }
   }
   ```

   * 如果当前的Profile设置为`test`，则Spring容器会调用`createZoneIdForTest()`创建`ZoneId`，否则，调用`createZoneId()`创建`ZoneId`。
   * 注意到`@Profile("!test")`表示非test环境。
   * 在运行程序时，加上JVM参数`-Dspring.profiles.active=test`就可以指定以`test`环境启动。

2. 实际上，Spring允许指定多个Profile，例如：

   ```java
   -Dspring.profiles.active=test,master
   ```

   * 可以表示`test`环境，并使用`master`分支代码。

   要满足多个Profile条件，可以这样写：

   ```java
   @Bean
   @Profile({ "test", "master" }) // 同时满足test和master
   ZoneId createZoneId() {
       ...
   }
   ```

3. 使用 Conditional

   除了根据`@Profile`条件来决定是否创建某个Bean外，Spring还可以根据`@Conditional`决定是否创建某个Bean。

   ```java
   @Component
   @Conditional(OnSmtpEnvCondition.class)
   public class SmtpMailService implements MailService {
       ...
   }
   ```

   * 它的意思是，如果满足`OnSmtpEnvCondition`的条件，才会创建`SmtpMailService`这个Bean。`OnSmtpEnvCondition`的条件是什么呢？我们看一下代码：

     ```java
     public class OnSmtpEnvCondition implements Condition {
         public boolean matches(ConditionContext context, AnnotatedTypeMetadata metadata) {
             return "true".equalsIgnoreCase(System.getenv("smtp"));
         }
     }
     ```

     因此，`OnSmtpEnvCondition`的条件是存在环境变量`smtp`，值为`true`。这样，我们就可以通过环境变量来控制是否创建`SmtpMailService`。

   Spring只提供了`@Conditional`注解，具体判断逻辑还需要我们自己实现。Spring Boot提供了更多使用起来更简单的条件注解，例如，如果配置文件中存在`app.smtp=true`，则创建`MailService`：

   ```java
   @Component
   @ConditionalOnProperty(name="app.smtp", havingValue="true")
   public class MailService {
       ...
   }
   ```

   

4. 小结

   1. Spring允许通过`@Profile`配置不同的Bean；
   2. Spring还提供了`@Conditional`来进行条件装配，Spring Boot在此基础上进一步提供了基于配置、Class、Bean等条件进行装配。



### 使用 AOP



### 访问数据库



### 开发 Web 应用



### 集成第三方组件





## Reference

* [Spring 开发](https://www.liaoxuefeng.com/wiki/1252599548343744/1266263217140032)
* 



