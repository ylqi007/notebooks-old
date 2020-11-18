[TOC]

## Building a RESTful Web Service

* In Spring's approach to building RESTful web services, HTTP requests are handled by a controller. These components are identified by the `@RestController` annotation, and the `GreetingController` handles `GET` requests for `/greeting` by returning a new instance of the `Greeting` class.

* This controller is concise and simple, but there is plenty going on under the hood.

  ```java
  package com.example.restservice;
  
  import java.util.concurrent.atomic.AtomicLong;
  
  import org.springframework.web.bind.annotation.GetMapping;
  import org.springframework.web.bind.annotation.RequestParam;
  import org.springframework.web.bind.annotation.RestController;
  
  @RestController
  public class GreetingController {
  
  	private static final String template = "Hello, %s!";
  	private final AtomicLong counter = new AtomicLong();
  
  	@GetMapping("/greeting")
  	public Greeting greeting(@RequestParam(value = "name", defaultValue = "World") String name) {
  		return new Greeting(counter.incrementAndGet(), String.format(template, name));
  	}
  }
  ```

  * The `@GetMapping` annotation ensures that HTTP GET requests to `/greeting` are mapped to the `greeting()` method.
  * `@RequestParam` binds the value of **the query string parameter `name`** into the `name` parameter of the `greeting()` method. If the `name` parameter is absent in the request, the `defaultValue` of `World` is used.
  * The implementation of the method body creates and returns a new `Greeting` object with `id` and `content` attributes.

* A key difference between **a traditional MVC controller** and **the RESTful web service controller** is the way that the HTTP response body is created.

  * MVC: Rely on a view technology to perform server-side rendering of the greeting data to HTML;
  * RESTful web service controller populates and returns a `Greeting` object. The object data will be written directly to the HTTP response as JSON.

* This code uses Spring [`@RestController`](https://docs.spring.io/spring/docs/current/javadoc-api/org/springframework/web/bind/annotation/RestController.html) annotation, which marks the class as a controller where every method  returns a domain object instead of a view. It is shorthand for including both `@Controller` and `@ResponseBody`. 



## Building Java Projects with maven

* **INFO:** Projects downloaded from [Spring Initializr](https://start.spring.io) have the **wrapper** included. It shows up as a script `mvnw` in the top level of your project which you run in place of `mvn`.

### Define a simple Maven build

> Now that Maven is installed, you need to create a Maven project definition. Maven projects are defined with an XML file named *pom.xml*. Among other things, this file gives the project’s name, version, and dependencies that it has on external libraries.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>org.springframework</groupId>
    <artifactId>gs-maven</artifactId>
    <packaging>jar</packaging>
    <version>0.1.0</version>

    <properties>
        <maven.compiler.source>1.8</maven.compiler.source>
        <maven.compiler.target>1.8</maven.compiler.target>
    </properties>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>3.2.4</version>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
                        <configuration>
                            <transformers>
                                <transformer
                                    implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                                    <mainClass>hello.HelloWorld</mainClass>
                                </transformer>
                            </transformers>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

It includes the following details of the project configuration:

- `<modelVersion>`. POM model version (always 4.0.0).
- `<groupId>`. Group or organization that the project belongs to. Often expressed as an inverted domain name.
- `<artifactId>`. Name to be given to the project’s library artifact (for example, the name of its JAR or WAR file).
- `<version>`. Version of the project that is being built.
- `<packaging>` - How the project should be packaged. Defaults to "jar" for JAR file packaging. Use "war" for WAR file packaging.

### Build Java code

To try out the build, issue the following at the command line:

```bash
mvn compile
```

This will run Maven, telling it to execute the *compile* goal. When it's finished, you should find the compiled `.class` files in the *target/classes* directory.

### Declare Dependencies

This block of XML declares a list of dependencies for the project.  Specifically, it declares a single dependency for the Joda Time library. Within the `<dependency>` element, the dependency coordinates are defined by three sub-elements:

- `<groupId>` - The group or organization that the dependency belongs to.
- `<artifactId>` - The library that is required.
- `<version>` - The specific version of the library that is required.

By default, all dependencies are scoped as `compile` dependencies. That is, they should be available at compile-time (and if you were building a WAR file, including in the */WEB-INF/libs* folder of the WAR). Additionally, you may specify a `<scope>` element to specify one of the following scopes:

- `provided` - Dependencies that are required for  compiling the project code, but that will be provided at runtime by a  container running the code (e.g., the Java Servlet API).
- `test` - Dependencies that are used for compiling and running tests, but not required for building or running the project’s  runtime code.

Now if you run `mvn compile` or `mvn package`, Maven should resolve the Joda Time dependency from the Maven Central repository and the build will be successful.





## Reference

* [Building a RESTful Web Service](https://spring.io/guides/gs/rest-service/)
* [构建一个RESTful Web服务](http://www.spring4all.com/article/845)
* [Building Java Projects with Maven](https://spring.io/guides/gs/maven/#initial)
* [基于Maven来构建Java项目](http://www.spring4all.com/article/538)
* 







