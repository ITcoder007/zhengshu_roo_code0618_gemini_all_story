

### **故事文件: story-1.1.md**

## Status: Approved

## 故事

- **作为一个**开发者，
- **我想要**一个设置好的、包含前后端模块的Monorepo项目结构，
- **以便于**我有一个干净、可立即投入开发的基础环境。

## 验收标准 (ACs)

1. 一个空的 Monorepo 仓库被初始化。
2. 仓库中包含一个后端模块，使用**Maven**和 Spring Boot 2.7.x 进行配置。
3. 仓库中包含一个前端模块，使用 Vue 3.x 进行配置。
4. 前后端应用都可以在本地独立启动。
5. 根目录包含一个基础的`README.md`文件。

## 任务 / Subtasks

- [ ] 1. 初始化Git仓库并设置Monorepo结构。
- [ ] 2. 使用Spring Initializr创建后端Maven项目模块 (`/backend`)，集成MybatisPlus 3.5.x。
- [ ] 3. 使用Vite创建前端Vue 3.x项目模块 (`/frontend`)。
- [ ] 4. 创建根`README.md`并添加项目启动说明。

## Dev Notes

- **架构参考**: 遵循架构文档中定义的Monorepo源代码结构。

### 测试

- 本故事的验证方式是确保`mvn spring-boot:run`和`npm run serve`命令能成功启动，无编译错误。

## Dev Agent Record

### Agent Model Used:

### Debug Log References:

### Completion Notes List:

### Change Log:

---

### **故事文件: story-1.2.md**

## Status: Approved

## 故事

- **作为一个**开发者，
- **我想要**配置好测试驱动开发（TDD）所需的环境，以及一个基础的持续集成（CI）流水线，
- **以便于**我从项目一开始就能保障代码质量并自动化构建与测试。

## 验收标准 (ACs)

1. 后端模块中集成了JUnit 5测试框架。
2. 前端模块中集成了**Jest**测试框架。
3. 代码仓库中配置一个基础的CI脚本（如GitHub Actions），在代码提交时能自动执行测试。
4. 代码覆盖率工具已集成，并设定了**80%**的目标。

## 任务 / Subtasks

- [ ] 1. (后端) 在`backend/pom.xml`中配置Jacoco插件，设定80%的覆盖率检查规则，并配置报告生成。
- [ ] 2. (前端) 在`frontend`目录中安装Jest及相关依赖，配置测试环境。
- [ ] 3. (前端) 创建`frontend/jest.config.js`并配置好覆盖率报告和80%的阈值检查。
- [ ] 4. (CI) 在项目根目录创建`.github/workflows/ci.yml`文件，包含代码质量检查。
- [ ] 5. (CI) 在`ci.yml`中编写脚本，依次执行后端 (`mvn clean verify`) 和前端 (`npm test`) 的测试命令，并收集覆盖率报告。

## Dev Notes

- **TDD要求**: 严格遵循TDD模式，先编写测试用例，再实现功能代码。
- **质量门禁**: 测试覆盖率必须达刅80%，否则CI流水线失败。
- **CI**: 流水线应在代码`push`到主分支时自动触发，包含测试、覆盖率检查和代码质量分析。

### 测试

- 本故事的验证方式是CI流水线能够成功运行，测试覆盖率达刅80%，并生成详细的质量报告。流水线失败时应阻止代码合并。

## Dev Agent Record

### Agent Model Used:

### Debug Log References:

### Completion Notes List:

### Change Log:

---

### **故事文件: story-1.3.md**

## Status: Approved

## 故事

- **作为一个**开发者，
- **我想要**将后端服务与MySQL 8.0数据库成功集成，并定义核心的`Certificate`领域模型，
- **以便于**系统能够持久化存储证书数据。

## 验收标准 (ACs)

1. 后端应用能够成功连接到MySQL 8.0数据库。
2. 定义了`Certificate`实体，包含PRD中所有字段。
3. 通过SQL初始化脚本，在数据库中创建了`certificates`表。
4. `domain`字段有唯一约束。

## 任务 / Subtasks

- [ ] 1. 在`backend/src/main/resources/application.properties`中添加MySQL数据源配置，包含时区设置(serverTimezone=Asia/Shanghai)。
- [ ] 2. 创建`Certificate.java`实体类，包含所有必需的字段和JPA/MybatisPlus注解。
- [ ] 3. 创建一个SQL初始化脚本（如`schema.sql`），定义`certificates`表结构。
- [ ] 4. 创建`CertificateRepository.java`接口，用于数据访问。

## Dev Notes

- **数据表结构**: 严格遵循架构文档中定义的SQL`CREATE TABLE`语句。
- **领域模型**:`Certificate`实体应放在`domain`包下，Repository接口也应在`domain`包下。
- **数据库配置**: 使用连接字符串`jdbc:mysql://localhost:3306/cert_claude_code0624_2?useUnicode=true&characterEncoding=utf-8&serverTimezone=Asia/Shanghai`确保时区正确。

### 测试

- 需编写一个集成测试，验证应用启动时能连接数据库，并能成功通过Repository保存和读取一个`Certificate`实体。

## Dev Agent Record

### Agent Model Used:

### Debug Log References:

### Completion Notes List:

### Change Log:

---

### **故事文件: story-1.4.md**

## Status: Approved

## 故事

- **作为一个**用户，
- **我想要**一套完整的RESTful API来对证书元数据进行增、删、改、查操作，
- **以便于**我可以通过接口管理我的所有证书资产。

## 验收标准 (ACs)

1. 提供`POST /api/certificates`端点。
2. 提供`GET /api/certificates`和`GET /api/certificates/{id}`端点。
3. 提供`PUT /api/certificates/{id}`端点。
4. 提供`DELETE /api/certificates/{id}`端点。
5. 所有端点返回统一结构的响应体。
6. 所有端点都通过 Swagger 3.0.x 进行了文档化。
7. CRUD操作能正确更新审计字段（creator和modifier默认为"admin"）。

## 任务 / Subtasks

- [ ] 1. 创建`CertificateController.java`并实现上述5个API端点。
- [ ] 2. 为每个端点添加Swagger注解。
- [ ] 3. 实现对应的应用服务逻辑，处理DTO转换和业务协调。
- [ ] 4. 确保在创建和更新时，自动填充审计字段（`creator`和`modifier`默认为"admin",`createdAt`和`modifiedAt`自动设置当前时间）。

## Dev Notes

- **API规格**: 严格遵循架构文档中定义的“可读版API规格”，包括URL、方法、请求体和响应结构。
- **统一响应体**: 创建一个泛型的`ApiResponse<T>`类来封装所有返回数据。

### 测试

- 需要为`CertificateController`编写集成测试，覆盖所有端点的成功和失败（如404 Not Found）场景。

## Dev Agent Record

### Agent Model Used:

### Debug Log References:

### Completion Notes List:

### Change Log:

---

### **故事文件: story-2.0.md**

## Status: Approved

## 故事

- **作为一个**用户，
- **我想要**直接在看板页面上发起对证书的增、改、删操作，
- **以便于**我的管理工作流程更加高效和连贯。

## 任务 / Subtasks

- [ ] 1. 创建一个`CertificateForm.vue`组件，包含域名和过期日的输入表单。
- [ ] 2. 在`Dashboard.vue`中添加“新增证书”按钮，点击后以模态框形式显示`CertificateForm`。
- [ ] 3. 为证书列表的每一行添加“编辑”和“删除”按钮。
- [ ] 4. 实现点击“编辑”按钮时，打开`CertificateForm`模态框并填充数据。
- [ ] 5. 实现点击“删除”按钮时，弹出二次确认对话框。
- [ ] 6. 在`CertificateForm`中实现提交逻辑，根据是新增还是编辑，调用对应的POST或PUT API。
- [ ] 7. 实现删除逻辑，调用DELETE API。
- [ ] 8. 在任何操作（增/改/删）成功后，刷新看板的证书列表。

## Dev Notes

- **组件复用**:`CertificateForm.vue`应该被设计为可同时用于新增和编辑两种场景。
- **用户反馈**: 所有操作成功或失败后，都应有明确的用户提示（如Toast通知）。

### 测试

- 为`CertificateForm.vue`编写组件测试，验证表单提交时是否会触发带有正确数据的API调用事件。
- 为`Dashboard.vue`编写组件测试，验证点击增/改/删按钮后是否会触发正确的行为（如打开模态框、调用删除API）。

## Dev Agent Record

### Agent Model Used:

### Debug Log References:

### Completion Notes List:

### Change Log:

---

### **故事文件: story-2.1.md**

## Status: Approved

## 故事

- **作为一个**用户，
- **我想要**一个基础的看板页面，它能从后端获取并展示我的证书列表，
- **以便于**我有一个集中的地方来查看我的所有资产。

## 任务 / Subtasks

- [ ] 1. 在前端项目中创建`Dashboard.vue`视图文件。
- [ ] 2. 在Vue Router中添加`/dashboard`路由。
- [ ] 3. 创建一个`apiService.js`模块，用于封装对后端API的调用。
- [ ] 4. 配置Pinia状态管理器，用于管理证书列表状态。
- [ ] 5. 在`Dashboard.vue`的`onMounted`生命周期钩子中调用API获取证书列表。
- [ ] 6. 将获取的数据展示在一个基础的HTML`<table>`中。
- [ ] 7. 添加简单的加载中和加载失败的文本提示。

## Dev Notes

- **API端点**: 调用`GET /api/certificates`。
- **状态管理**: 使用Pinia来管理证书列表的状态。

### 测试

- 使用Jest编写`Dashboard.vue`的组件测试，模拟API调用，验证：
    - 组件在加载时是否正确显示“加载中”。
    - API成功返回后是否正确渲染表格。
    - API失败后是否正确显示错误信息。

## Dev Agent Record

### Agent Model Used:

### Debug Log References:

### Completion Notes List:

### Change Log:

---

### **故事文件: story-2.2.md**

## Status: Approved

## 故事

- **作为一个**用户，
- **我想要**在看板的列表中看到每个证书的健康状态，这个状态应该是实时计算的，
- **以便于**我能快速识别出哪些证书需要立即关注。

## 任务 / Subtasks

- [ ] 1. 创建一个`utils/statusCalculator.js`工具函数，输入过期日，返回状态字符串（'正常', '警告'等）。
- [ ] 2. 创建一个`StatusTag.vue`组件，根据传入的状态显示不同颜色（如绿色、黄色、红色）的标签。
- [ ] 3. 在`Dashboard.vue`的表格中新增“状态”列，并使用`StatusTag`组件来展示计算出的状态。
- [ ] 4. 将“平安橙”作为系统的主题色，应用到关键UI元素上（如按钮、标题）。

## Dev Notes

- **状态计算规则**:`≥30天: 正常(绿)`,`7-29天: 警告(黄)`,`1-6天: 紧急(橙)`,`≤0天: 危险(红)`。
- **颜色**: “平安橙”可作为“紧急”状态的颜色。

### 测试

- 为`statusCalculator.js`编写单元测试，覆盖所有状态计算的边界条件。
- 为`StatusTag.vue`编写组件快照测试，确保不同状态下渲染的颜色和文本正确。

## Dev Agent Record

### Agent Model Used:

### Debug Log References:

### Completion Notes List:

### Change Log:

---

### **故事文件: story-2.3.md**

## Status: Approved

## 故事

- **作为一个**用户，
- **我想要**对看板上的证书列表进行排序和搜索，
- **以便于**我能快速地从大量证书中定位到我需要的信息。

## 任务 / Subtasks

- [ ] 1. 在`Dashboard.vue`中添加一个搜索输入框。
- [ ] 2. 为表格的“过期日”列标题添加点击事件。
- [ ] 3. 修改`apiService.js`中的证书获取函数，使其能够接收并传递`search`和`sortBy`等查询参数。
- [ ] 4. 在`Dashboard.vue`中添加逻辑，当用户输入搜索词或点击排序时，使用新的参数重新调用API。

## Dev Notes

- **防抖 (Debounce)**: 建议为搜索输入框添加防抖功能，以避免频繁发送API请求。
- **API参数**: 后端API支持`sortBy=expiryDate`和`search=...`参数（域名模糊搜索）。

### 测试

- 编写`Dashboard.vue`的组件测试，验证当用户进行搜索或排序操作时，`apiService`的调用函数是否被以正确的参数调用。

## Dev Agent Record

### Agent Model Used:

### Debug Log References:

### Completion Notes List:

### Change Log:


