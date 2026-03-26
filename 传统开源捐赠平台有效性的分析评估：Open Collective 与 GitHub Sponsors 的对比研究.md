# 传统开源捐赠平台有效性的分析评估：Open Collective 与 GitHub Sponsors 的对比研究（优化扩展稿）

## 摘要

开源软件已成为数字经济与公共数字基础设施的核心，但其维护投入与资金回流长期失衡。围绕“平台化捐赠是否真正提升开源可持续性”这一问题，本文比较 Open Collective（组织化透明治理导向）与 GitHub Sponsors（开发者个体与平台流量导向）两类主流模式，构建“**转化—稳定—治理—公平**”四维有效性框架，并提出 3 个可检验研究问题（RQ）及对应实验设计。研究采用“文献归纳 + 平台机制比较 + 观测数据实证设计”的混合方法：一方面系统梳理资金流、治理结构、费用机制与激励路径；另一方面设计准实验（配对+双重差分）、事件研究和不平等测度实验（Gini/Theil/Top-share）检验平台在不同项目类型与生命周期阶段的效果差异。研究预期表明：GitHub Sponsors 在初期资金转化率与轻量化接入上更具优势；Open Collective 在资金可审计性、团队协作分配与组织合规方面更优；两者均存在“头部集中”与长期稳定性不足问题。基于此，本文提出“**双平台筹资 + 统一披露口径 + 产出绑定评价**”的混合治理路线，为维护者、基金会与平台运营者提供可操作策略。

**关键词：** 开源可持续性；Open Collective；GitHub Sponsors；平台有效性；资金治理；数字公共品

---

## 1. 研究背景与问题提出

### 1.1 问题背景

开源生态面临典型的公共品困境：社会整体收益高，但维护劳动回报低且不稳定。已有研究与产业报告持续指出，维护者收入不确定性、倦怠和退出风险，是影响软件供应链安全与创新韧性的关键瓶颈。与传统“捐一次算一次”的零散支持相比，平台化捐赠机制通过降低支付摩擦、提升可见性与关系维护能力，正在重塑开源筹资结构。

### 1.2 研究对象与比较价值

- **Open Collective（OC）**：依赖 Fiscal Host（财务托管主体）实现资金代持、合规与公开记账，强调预算透明、组织治理与多角色协作。
- **GitHub Sponsors（GHS）**：嵌入代码协作平台，以开发者主页、仓库场景与订阅机制强化赞助转化和持续支持。

二者并非简单替代，而是在“低摩擦转化”与“高透明治理”之间提供不同制度组合，适合不同发展阶段和治理需求的开源项目。

### 1.3 研究目标

本文目标是从“是否募到钱”进一步推进到“是否形成可持续、可问责、相对公平的资金循环”，并提出可落地的实证研究方案，满足学术论文对“可检验性”和“可复现性”的要求。

---

## 2. 文献综述与研究缺口

### 2.1 开源资金可持续性文献

- 开源贡献与商业收益之间存在结构性错配，长期维护劳动常被低估。
- 维护者报酬与安全质量存在正相关倾向（被支付维护者通常更能持续投入维护工作）。
- 平台赞助机制（如 GHS）有助于建立经常性支持，但存在参与门槛、曝光不均与头部集中现象。

### 2.2 平台机制与治理文献

- OC 文档与相关研究强调财政托管、预算透明和公共问责的重要性。
- GHS 文档强调赞助门槛低、个人账户赞助低费用（或免平台费）等转化优势。
- 已有个案研究多聚焦“谁获得赞助”，对“**资金进入后如何治理与分配**”关注不足。

### 2.3 研究缺口

1. **指标缺口**：多数研究只比较筹资额，缺少治理与公平维度。
2. **方法缺口**：缺乏“平台迁移/并行使用”情景下的准实验识别。
3. **决策缺口**：缺少“项目阶段—平台能力”匹配模型与实证支持。

---

## 3. 理论框架与研究问题（RQ）

## 3.1 理论框架：四维有效性模型

本文将平台有效性定义为：在给定交易成本与治理约束下，平台持续促成**可进入（Conversion）—可持续（Stability）—可问责（Governance）—相对公平（Equity）**资金循环的能力。

- **C（Conversion）转化维度**：捐赠触达、转化成本、赞助启动速度。
- **S（Stability）稳定维度**：月度留存、收入波动、抗冲击能力。
- **G（Governance）治理维度**：资金流透明度、预算约束、可审计性。
- **E（Equity）公平维度**：跨角色分配、头部集中度、贡献-收益匹配。

## 3.2 研究问题（3 个 RQ）

**RQ1（转化与稳定）：** 相比 OC，GHS 是否显著提升项目的早期捐赠转化与短期收入增长？其增益能否在 6–12 个月维持？

**RQ2（治理与协作）：** 相比 GHS，OC 是否显著提升资金流透明度、团队协作分配覆盖率和非代码贡献者的可见性？

**RQ3（公平与结构）：** 两平台在赞助分布上是否均存在马太效应？若存在，何种治理与披露机制可降低资金过度集中？

## 3.3 研究假设（可选）

- **H1**：GHS 在平台上线后前 3 个月的新增赞助数增长率高于 OC。
- **H2**：OC 在“可公开支出条目比例”“跨角色受益人数占比”上显著高于 GHS。
- **H3**：两平台均表现出头部集中，但 OC 的治理机制可在团队项目中部分缓解集中度。

---

## 4. 研究设计：数据、变量与实验方案

## 4.1 数据来源与样本构建

- **平台数据**：
  - GHS：公开 Sponsors 页面、层级信息、项目仓库元数据（Stars/Forks/Contributors/Release）。
  - OC：Collective 公开账本、收入/支出条目、预算说明、Host 信息。
- **补充数据**：项目活跃度（提交频率、Issue 处理时延、版本发布节奏）、社交传播信号（如 X/Twitter 提及事件）。
- **样本分层**：个人项目、小团队项目、基金会/联盟项目三类；按项目年龄和规模分层抽样。

## 4.2 核心变量定义

- **因变量（Y）**：月度赞助额、赞助者净增长、续捐率、收入波动系数、Gini/Theil、可公开支出占比。
- **处理变量（T）**：平台采用状态（仅 GHS / 仅 OC / 双平台），及切换时间点。
- **控制变量（X）**：仓库受欢迎度、活跃度、语言生态、组织属性、外部事件（重大漏洞、版本发布）。

## 4.3 实验设计 A：RQ1（准实验）

**目标**：识别 GHS 对早期转化与短期增长的影响。

- **方法**：倾向得分匹配（PSM）+ 双重差分（DID）。
- **处理组**：在观察窗内新开通 GHS 的项目。
- **对照组**：未开通 GHS、但在规模/活跃度/领域相近项目。
- **模型示意**：
  \[
  Y_{it}=\alpha + \beta (Treat_i \times Post_t) + \gamma X_{it}+\mu_i+\lambda_t+\epsilon_{it}
  \]
- **判定**：\(\beta>0\) 且显著支持 H1。

## 4.4 实验设计 B：RQ2（治理绩效比较）

**目标**：检验 OC 在治理透明与团队分配上的优势。

- **方法**：
  1) 构建“治理透明度指数 GTI”（公开支出粒度、预算说明完整度、可追溯性、更新时间）；
  2) 构建“协作分配指数 CDI”（受益角色多样性、非代码角色覆盖、资金用途清晰度）。
- **比较策略**：对仅 OC、仅 GHS、双平台项目进行分层回归与稳健性检验。
- **判定**：OC 组 GTI/CDI 显著高于 GHS 组支持 H2。

## 4.5 实验设计 C：RQ3（公平性与马太效应）

**目标**：评估资金集中及其变化机制。

- **方法**：
  - 计算每个平台内项目级赞助分布的 Gini、Theil、Top 1%/10% 份额；
  - 事件研究：分析“引入公开预算模板/分配规则”前后集中度变化；
  - 分位数回归：识别中尾部项目是否受益。
- **判定**：若集中度长期升高且中尾部项目改善有限，则验证“平台化不必然带来分配公平”。

## 4.6 稳健性与效度威胁处理

- **选择偏差**：采用 PSM、固定效应、替代匹配算法。
- **反向因果**：使用滞后变量与安慰剂检验。
- **外生冲击**：加入时间固定效应与重大事件虚拟变量。
- **数据缺失**：多重插补与删失敏感性分析。

---

## 5. 机制比较：Open Collective vs GitHub Sponsors

| 比较维度 | Open Collective | GitHub Sponsors | 学术解释 |
|---|---|---|---|
| 进入门槛 | 需理解 Host/Collective 结构 | 入口贴近 GitHub 账号和仓库 | GHS 降低初始转化摩擦 |
| 资金透明 | 强（公开账本、支出可追踪） | 中（赞助公开与否可配置，支出链路通常不完整） | OC 强于治理问责 |
| 组织协作 | 强（多角色预算分配） | 中（更偏个人或组织主页赞助） | OC 对团队更友好 |
| 续捐机制 | 可做预算叙事与公开反馈 | 订阅层级成熟，依赖维护者曝光 | 两者均可，但驱动机制不同 |
| 合规与托管 | Fiscal Host 提供法务/税务支持 | 更多依赖账号主体与外部财税安排 | OC 对“无实体团队”更关键 |

---

## 6. 预期结果与讨论（写作模板）

> 本节用于在获得数据后填入实证结果。以下为建议写法。

### 6.1 RQ1 预期

预计 GHS 在上线初期（1–3 个月）显著提升赞助转化，但增速在 6 个月后趋于回落，表现出“启动快、维持难”的典型平台效应。

### 6.2 RQ2 预期

预计 OC 在治理透明度（GTI）和协作分配指数（CDI）上显著高于 GHS，尤其在小团队和基金会型项目更明显。

### 6.3 RQ3 预期

预计两平台均出现头部集中，但 OC 中“预算公开+角色分配”机制可对集中趋势产生缓冲；GHS 受“可见度—赞助”正反馈影响更强。

### 6.4 理论贡献

- 将开源捐赠研究从“金额中心”推进到“制度绩效中心”；
- 提供可复现的四维指标体系与准实验识别框架；
- 为平台设计提供“转化效率—治理质量”权衡视角。

---

## 7. 实务与政策建议

### 7.1 对维护者/项目方

1. **早期阶段**：优先用 GHS 建立低摩擦月捐入口。
2. **协作扩展阶段**：引入 OC 构建可审计预算与报销机制。
3. **稳定运营阶段**：双平台并行，但采用统一披露面板（收入、支出、里程碑、风险）。

### 7.2 对平台运营者

1. 建立跨平台数据接口，支持统一指标看板；
2. 提供“非代码贡献者”收益模板，降低隐性劳动被忽视；
3. 引入反集中激励（中尾部项目曝光扶持、匹配捐赠）。

### 7.3 对基金会/政策制定者

1. 建立关键开源基础设施的稳定资助池与逆周期机制；
2. 推动开源项目披露标准化（支出、角色、产出）；
3. 将开源回馈纳入企业采购、合规与 ESG 评估体系。

---

## 8. 论文写作规范补强（可直接用于正式稿）

- **方法章节补强**：明确样本期、排除标准、统计功效（power）与显著性阈值。
- **结果章节补强**：提供主回归+稳健性回归+异质性分析（项目规模/语言/组织属性）。
- **图表清单建议**：
  - 图1：研究框架图（C-S-G-E）；
  - 图2：平台资金流机制图；
  - 图3：事件研究动态效应图；
  - 表1：变量定义；
  - 表2：描述性统计；
  - 表3：RQ1 回归结果；
  - 表4：RQ2 指数比较；
  - 表5：RQ3 不平等指标与分位数回归。
- **复现性附件**：附数据字典、代码仓库链接、指标计算脚本说明。

---

## 参考文献（基于“相关文献.docx”整理的可用核心清单，建议正式投稿前统一为 GB/T 7714）

1. GitHub Docs. *About GitHub Sponsors*. https://docs.github.com/en/sponsors/getting-started-with-github-sponsors/about-github-sponsors  
2. GitHub Docs. *GitHub Sponsors documentation*. https://docs.github.com/en/sponsors  
3. Open Collective Docs. *Fiscal Hosts*. https://documentation.opencollective.com/fiscal-hosts/fiscal-hosts  
4. Open Collective Docs. *Choosing a Fiscal Host*. https://documentation.opencollective.com/collectives/choosing-a-fiscal-host  
5. Open Source Collective Docs. *GitHub Sponsors*. https://docs.oscollective.org/campaigns-and-partnerships/github-sponsors  
6. Zhou, et al. *A Case Study of GitHub Projects Collecting Donations...* (EMSE, 2021). https://posl.ait.kyushu-u.ac.jp/~kamei/publications/Zhou_EMSE2021.pdf  
7. “Who, What, Why and How? Towards the Monetary Incentive in Crowd Collaboration: A Case Study of GitHub’s Sponsor Mechanism”. https://arxiv.org/abs/2111.13323  
8. “My GitHub Sponsors profile is live!” Investigating the Impact of Twitter/X Mentions on GitHub Sponsors. https://arxiv.org/html/2401.02755v1  
9. Tidelift. *The 2024 State of the Open Source Maintainer Report*. https://assets-eu-01.kc-usercontent.com/ef593040-b591-0198-9506-ed88b30bc023/d325a56f-05be-4379-bfd1-ee4776fcad41/2024-tidelift-state-of-the-open-source-maintainer-report-.pdf  
10. HBS Working Paper. *The Value of Open Source Software*. https://www.hbs.edu/ris/Publication%20Files/24-038_51f8444f-502c-4139-8bf2-56eb4b65c58a.pdf  
11. The Matthew effect in empirical data. https://pmc.ncbi.nlm.nih.gov/articles/PMC4233686/  
12. The Matthew effect in science funding. https://pmc.ncbi.nlm.nih.gov/articles/PMC5948972/  
13. A Toolkit for Measuring the Impacts of Public Funding on Open Source Software Development. https://arxiv.org/abs/2411.06027  
14. Funding Europe’s Open Digital Infrastructure. https://openforumeurope.org/wp-content/uploads/2025/10/EU-STF-Feasibility-Study_final.pdf  

---

## 附录 A：面向论文实证的执行清单

- [ ] 明确样本期（建议 24–36 个月）
- [ ] 完成平台项目映射（GHS/OC/双平台）
- [ ] 定义 GTI/CDI 指标并进行标注一致性检验（Cohen’s Kappa）
- [ ] 完成 PSM 匹配与平衡性检验
- [ ] 运行 DID、事件研究、分位数回归
- [ ] 完成稳健性与安慰剂检验
- [ ] 输出可复现附录（数据字典+代码）

## 附录 B：可直接写入“研究问题与方法”章节的精简版段落

本文提出三个研究问题：RQ1 关注平台对筹资转化与稳定性的影响，RQ2 关注平台对治理透明与协作分配的影响，RQ3 关注平台是否加剧或缓解资金集中。方法上，本文采用配对样本双重差分识别平台采用效应，构建治理透明度指数（GTI）与协作分配指数（CDI）评估治理绩效，并以 Gini、Theil 与 Top-share 指标测度马太效应，同时结合事件研究与分位数回归进行机制识别和异质性分析。该设计可在“转化效率—治理质量—分配公平”三条主线上形成可检验、可复现、可比较的证据链。
