# 错误记录与解决方案

## 1. Swagger UI显示默认页面而非API文档
**错误现象**：访问/swagger-ui.html显示默认页面而非控制器API文档  
**原因分析**：
- 缺少包扫描配置
- 未正确配置GroupedOpenApi
- 缺少必要的注解(@OpenAPIDefinition等)

**解决方案**：
1. 在OpenApiConfig中添加：
```java
@Bean
public GroupedOpenApi publicApi() {
    return GroupedOpenApi.builder()
            .group("public")
            .packagesToScan("com.example.backend.controller")
            .build();
}
```
2. 添加类级注解：
```java
@OpenAPIDefinition(info = @Info(title = "API文档", version = "1.0"))
@SecurityScheme(name = "bearerAuth", scheme = "bearer", type = SecuritySchemeType.HTTP)
```

**预防措施**：
- 新项目初始化时立即配置Swagger基础设置
- 使用Swagger注解规范标记所有控制器方法

## 2. 端口8080被占用
**错误现象**：应用启动时报端口冲突  
**原因分析**：本地已有服务占用8080端口

**解决方案**：
1. 修改application.yml：
```yaml
server:
  port: 8081
```
2. 或终止占用进程：
```bash
lsof -i :8080
kill -9 [PID]
```

**预防措施**：
- 开发前检查常用端口占用情况
- 在配置文件中预留备用端口配置

## 3. 应用启动内存不足
**错误现象**：启动时报OOM错误  
**原因分析**：默认JVM堆内存设置过小

**解决方案**：
1. 修改启动命令：
```bash
mvn spring-boot:run -Dspring-boot.run.jvmArguments="-Xmx512m -Xms256m"
```

**预防措施**：
- 项目文档中记录推荐JVM参数
- 在CI/CD流程中配置标准内存参数

## 4. 数据库表名映射不一致
**错误现象**：实体类与数据库表名不匹配  
**原因分析**：MybatisPlus默认命名策略与数据库不匹配

**解决方案**：
1. 配置全局命名策略：
```yaml
mybatis-plus:
  global-config:
    db-config:
      table-prefix: t_
      column-underline: true
```

**预防措施**：
- 项目初期明确数据库命名规范
- 在文档中记录ORM映射规则

## 5. 验证不及时导致问题累积
**错误现象**：多个问题同时出现难以排查  
**原因分析**：未遵循小步验证原则

**解决方案**：
1. 实施"开发-验证"循环：
   - 每完成一个小功能立即验证
   - 使用Postman/Swagger进行接口测试
   - 提交前运行完整测试套件

**预防措施**：
- 在任务拆分时明确验证点
- 使用自动化测试保障基础功能