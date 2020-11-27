[toc]

## 7. Developing Web Applications

> Most web applications use the `spring-boot-starter-web` module to get up and running quickly.



### 7.1 The "Spring Web MVC Framework"

> The [Spring Web MVC framework](https://docs.spring.io/spring/docs/5.3.1/reference/html/web.html#mvc) (often referred to as “Spring MVC”) is a rich “model view controller” web framework. Spring MVC lets you create special `@Controller` or `@RestController` beans to handle incoming HTTP requests. Methods in your controller are mapped to HTTP by using `@RequestMapping` annotations.
>
> Spring MVC is part of the core Spring Framework, and detailed information is available in the [reference documentation](https://docs.spring.io/spring/docs/5.3.1/reference/html/web.html#mvc).

* Spring MVC: **Model View Controller**
* Spring MVC 使用 `@Controller` or `RestController` beans 去处理 HTTP 请求
* Controller 中的 method 通过 `@RequestMapping` annotation 映射到不同的 HTTP 请求
* [Spring Web MVC](https://docs.spring.io/spring-framework/docs/5.3.1/reference/html/web.html#mvc)



#### 7.1.1 Spring MVC Auto-configuration

> Spring Boot provides auto-configuration for Spring MVC that works well with most applications.
> Spring Boot 为 Spring MVC 提供了**自动配置**。



#### 7.1.2 HttpMessageConverters

> Spring MVC uses the `HttpMessageConverter` interface to  convert HTTP requests and responses. Sensible defaults are included out of the box. For example, objects can be automatically converted to JSON (by using  the Jackson library) or XML (by using the Jackson XML extension, if  available, or by using JAXB if the Jackson XML extension is not  available). By default, strings are encoded in `UTF-8`.
>
> Any `HttpMessageConverter` bean that is present in the context is added to the list of converters. You can also override default converters in the same way.

* Spring MVC 通过 `HttpMessageConveter` 接口转换 HTTP 请求和相应。
* 默认设置是开箱即用的。比如 objects 可以自动转换成 JSON or XML，默认的 strings 是用 `UTF-8` 编码。



#### 7.1.3 Custom JSON Serializers and Deserializers

> If you use Jackson to serialize and deserialize JSON data, you might want to write your own `JsonSerializer` and `JsonDeserializer` classes. Custom serializers are usually [registered with Jackson through a module](https://github.com/FasterXML/jackson-docs/wiki/JacksonHowToCustomSerializers), but Spring Boot provides an alternative `@JsonComponent` annotation that makes it easier to directly register Spring Beans.
>
> You can use the `@JsonComponent` annotation directly on `JsonSerializer`, `JsonDeserializer` or `KeyDeserializer` implementations. You can also use it on classes that contain serializers/deserializers as inner classes.
>
> Spring Boot also provides [`JsonObjectSerializer`](https://github.com/spring-projects/spring-boot/tree/v2.4.0/spring-boot-project/spring-boot/src/main/java/org/springframework/boot/jackson/JsonObjectSerializer.java) and [`JsonObjectDeserializer`](https://github.com/spring-projects/spring-boot/tree/v2.4.0/spring-boot-project/spring-boot/src/main/java/org/springframework/boot/jackson/JsonObjectDeserializer.java) base classes that provide useful alternatives to the standard Jackson versions when serializing objects.

* 可以通过编写自己的 `JsonSerializer` and `JsonDeserialier` class 用 Jackson (a library) serialize and deserialize JSON data。
* Spring Boot 提供了 `@JsonComponent` annotation 直接注册 Spring Beans，方式就是直接将 `@JsonComponent` annotation 直接添加到 `JsonSerializer`, `JsonDeserialier` or `KeyDeserializer`。
* **==registered with Jackson?==**



#### 7.1.4 MessageCodesResolver

> Spring MVC has a strategy for generating error codes for rendering error messages from binding errors: `MessageCodesResolver`. If you set the `spring.mvc.message-codes-resolver-format` property `PREFIX_ERROR_CODE` or `POSTFIX_ERROR_CODE`, Spring Boot creates one for you (see the enumeration in [`DefaultMessageCodesResolver.Format`](https://docs.spring.io/spring/docs/5.3.1/javadoc-api/org/springframework/validation/DefaultMessageCodesResolver.Format.html)).



#### 7.1.5 Static Content

> By default, Spring Boot serves static content from a directory called `/static` (or `/public` or `/resources` or `/META-INF/resources`) in the classpath or from the root of the `ServletContext`. It uses the `ResourceHttpRequestHandler` from Spring MVC so that you can modify that behavior by adding your own `WebMvcConfigurer` and overriding the `addResourceHandlers` method.
>
> By default, resources are mapped on `/**`, but you can tune that with the `spring.mvc.static-path-pattern` property.
>
> You can also customize the static resource locations by using the `spring.web.resources.static-locations` property (replacing the default values with a list of directory locations). The root Servlet context path, `"/"`, is automatically added as a location as well.
>
> In addition to the “standard” static resource locations mentioned earlier, a special case is made for [Webjars content](https://www.webjars.org/). Any resources with a path in `/webjars/**` are served from jar files if they are packaged in the Webjars format.
>
> Spring Boot also supports the advanced resource handling features  provided by Spring MVC, allowing use cases such as **cache-busting** static  resources or using version agnostic URLs for Webjars.

* static content 加载路径
  * `/static`
  * `/public`
  * `/resources`
  * `/META-INF/resources`
* 在默认设置中，资源是映射到 `/**`，但是可以通过调整 `spring.web.resources.static-pattern` 设置
* 什么是 ==**webjars content**==



#### 7.1.6 Welcome Page

> Spring Boot supports both static and templated welcome pages. It first looks for an `index.html` file in the configured static content locations. If one is not found, it then looks for an `index` template. If either is found, it is automatically used as the welcome page of the application.

* Spring Boot 会在 static content 加载路径下寻找 `index.html`，也就是在上述四个 static content 加载路径



#### 7.1.7 Path Matching and Content Negotiation

> Spring MVC can map incoming HTTP requests to handlers by looking at the  request path and matching it to the mappings defined in your application (for example, `@GetMapping` annotations on Controller methods).
>
> There are other ways to deal with HTTP clients that don’t consistently send proper "Accept" request headers. Instead of using suffix matching, we can use a query parameter to ensure that requests like `"GET /projects/spring-boot?format=json"` will be mapped to `@GetMapping("/projects/spring-boot")`.
>
> As of Spring Framework 5.3, Spring MVC supports several implementation  strategies for matching request paths to Controller handlers. It was previously only supporting the `AntPathMatcher` strategy, but it now also offers `PathPatternParser`. Spring Boot now provides a configuration property to choose and opt in the new strategy



#### 7.1.8 ConfigurableWebBindingInitializer



#### 7.1.9 Template Engines

> As well as REST web services, you can also use Spring MVC to serve dynamic HTML content. Spring MVC supports a variety of templating technologies, including Thymeleaf, FreeMarker, and JSPs. Also, many other templating engines include their own Spring MVC integrations.
>
> When you use one of these templating engines with the default configuration, your templates are picked up automatically from `src/main/resources/templates`.

* Spring MVC 可以处理动态 HTML 内容，并且支持一系列模板引擎，包括 Thymeleaf, FreeMarker, and JSPs. 
* Spring Boot 的自动配置支持一下四个模板引擎：
  * [FreeMarker](https://freemarker.apache.org/docs/)
  * [Groovy](https://docs.groovy-lang.org/docs/next/html/documentation/template-engines.html#_the_markuptemplateengine)
  * [Thymeleaf](https://www.thymeleaf.org)
  * [Mustache](https://mustache.github.io/)
* 当使用上述默认配置支持的模板引擎的时候，Spring Boot 会在 `src/main/resources/templates` 中自动寻找并加载模板。



#### 7.1.10 Error Handling

> By default, Spring Boot provides an `/error` mapping that handles all errors in a sensible way, and it is registered as a “global” error page in the servlet container.
>
> By default, Spring Boot provides an `/error` mapping that handles all errors in a sensible way, and it is registered as a “global” error page in the servlet container. For machine clients, it produces a JSON response with details of the error, the HTTP status, and the exception message. For browser clients, there is a “whitelabel” error view that renders the same data in HTML format (to customize it, add a `View` that resolves to `error`). To replace the default behavior completely, you can implement `ErrorController` and register a bean definition of that type or add a bean of type `ErrorAttributes` to use the existing mechanism but replace the contents.



##### Custom Error Pages

> If you want to display a custom HTML error page for a given status code, you can add a file to an `/error` directory. Error pages can either be static HTML (that is, added under any of the  static resource directories) or be built by using templates. The name of the file should be the exact status code or a series mask.



##### Mapping Error Pages outside of Spring MVC



##### Error handling in a war deployment



#### 7.1.11 Spring HATEOAS



#### 7.1.12 CORS Support



### 7.2 The "Spring WebFlux Framework"



### ...



## Reference

* [7. Developing Web Applications](https://docs.spring.io/spring-boot/docs/current/reference/html/spring-boot-features.html#boot-features-developing-web-applications)
* 