[toc]

### 1.5 Working with Spring Boot -- Maven

[Apache Maven Project](https://maven.apache.org/pom.html)

To use the Spring Boot Maven Plugin, include the appropriate XML in the plugins section of your pom.xml, as shown in the following example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
	https://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<!-- ... -->
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```



Maven users can inherit from the `spring-boot-starter-parent` project to obtain sensible defualts. To configure your project to inherit from the `spring-boot-starter-parent`, set the parent as follows:

```xml
<!-- Inherit defaults from Spring Boot -->
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.4.0</version>
</parent>
```

* **You should need to specify only the Spring Boot version number on this dependency.** If you import additional starters, you can safely omit the version number. 只需要指定 Spring Boot 版本即可。



### 3.2 Structuring Your Code

#### 3.2.1 Using the "default" package

>  When a class does not include a *package* declaration, it is considered to be in the "default" package. The use of the “default package” is generally discouraged and should be avoided. It can cause particular problems for Spring Boot applications that use the `@ComponentScan`, `@ConfigurationPropertiesScan`, `@EntityScan`, or `@SpringBootApplication` annotations, since every class from every jar is read
>
> * We recommend that you follow Java’s recommended package naming conventions and use a reversed domain name (for example, `com.example.project`)

建议在每个 class 内部引入 package declaration；根据命名传统可以使用 reversed domain name, like `com.example.project`



#### 3.2.2 Locating the Main Application Class

> We generally recommend that you locate your main application class in a **root package** above other classes. The `@SpringBootApplication` annotation is often placed on your **main class**, and it implicitly defines a **base “search package”** for certain items. 

```
com
    +- example
        +- myapplication
            +- Application.java
            |
            +- customer
            | +- Customer.java
            | +- CustomerController.java
            | +- CustomerService.java
            | +- CustomerRepository.java
            |
            +- order
                +- Order.java
                +- OrderController.java
                +- OrderService.java
                +- OrderRepository.java
```



### 3.3 Configuration Classes

> **Spring Boot favors Java-based configuration.** Although it is possible to use SpringApplication with XML sources, **we generally recommend that your primary source be a single `@Configuration` class.** Usually the class that defines the main method is a good candidate as the primary `@Configuration`.
>
> * Spring Boot 推荐 java-based 的 configuration。可以通过 `@Configuration` 注解定义一个配置类。
> * 通常而言，定义了 `main()` method 的 class，是个很好的用来定义配置的主要选择。



#### 3.3.1 Importing Additional Configuration Classes

> You need not put all your `@Configuration` into a single class. 不需要将所有的 configuration 放到一个单独的 class 中。
>
> The `@Import`annotation can be used to import additional configuration classes. 可以用 `@Import` 注解导入配置类。
>
> Alternatively, you can use `@ComponentScan` to automatically pick up all Spring components, including `@Configuration` classes. 也可以使用 `@ComponentScan` 自动扫描所有的 spring component，包括有 `@Configuration` 注解的类。



#### 3.3.2 Importing XML Configuratoin

> If you absolutely must use XML based configuration, we recommend that you still start with a `@Configuration` class. You can then use an @ImportResource annotation to load XML configuration files.



### 3.4 Auto-configuration

> Spring Boot auto-configuration attempts to automatically configure your Spring application based on the jar dependencies that you have added.
>
> You need to opt-in to auto-configuration by adding the `@EnableAutoConfiguration` or `@SpringBootApplication` annotations to one of your` @Configuration` classes. 可以通过在标有 `@Configuration` 的 class 上继续添加 `@EnableAutoConfiguration` or `@SpringBootApplication` 注解启用自动配置。
>
> * You should only ever add one annotation `@SpringBootApplication` or `@EnableAutoCongiguration`. We generally recommend that you add one or the other to your `@SpringBootApplication` or `@EnableAutoConfiguration` primary `@Configuration` class only. 只能添加 `@SpringBootApplication` or `@EnableAutoCongigur



#### 3.4.1 Gradually Replacing Auto-configuration



#### 3.4.2 Disabling Specific Auto-configuration Classes

> If you find that specific auto-configuration classes that you do not want are being applied, you can use the exclude attribute of `@SpringBootApplication` to disable them, as shown in the following example:
>
> ```java
> import org.springframework.boot.autoconfigure.*;
> import org.springframework.boot.autoconfigure.jdbc.*;
> 
> @SpringBootApplication(exclude={DataSourceAutoConfiguration.class})
> public class MyApplication {
> }
> ```

>  If the class is not on the classpath, you can use the excludeName attribute of the annotation and specify the fully qualified name instead. If you prefer to use `@EnableAutoConfiguration` rather than `@SpringBootApplication`, exclude and excludeName are also available.
>
> Finally, you can also control the list of auto-configuration classes to exclude by using the `spring.autoconfigure.exclude` property.



### 3.5 Spring Beans and Dependency Injection

> We often find that using `@ComponentScan` (to find your beans) and using `@Autowired` (to do constructor injection) works well.
>
> If you structure your code as suggested above (locating your application class in a root package), you can add `@ComponentScan` without any arguments. All of your application components (`@Component`, `@Service`, `@Repository`, `@Controller` etc.) are automatically registered as Spring Beans.



### 3.6 Using the `@SpringBootApplication` Annotation

> A single `@SpringBootApplication` annotation can be used to enable those three features, that is:
>
> * `@EnableAutoConfiguration`: enable Spring Boot’s auto-configuration mechanism
> * `@ComponentScan`: enable `@Component` scan on the package where the application is located (see the best practices)
> * `@Configuration`: allow to register extra beans in the context or import additional configuration classes