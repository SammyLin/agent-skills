# Product Development Workflow

Sammy × Mochi 產品開發 SOP。源自 Phonics Lab 的血淚教訓（2026-02-23）。

## 適用時機
當 Sammy 要開發新產品/app/網站時，照這套流程走。

---

## Phase 0：定義靈魂（開工前）

1. Sammy 描述**核心體驗**（一句話）
2. 截圖/畫草圖/找參考產品 → 存為設計基準
3. 寫下「**這個產品不做什麼**」
4. `git init` + 第一個 commit

## Phase 1：MVP（最小可用版本）

1. 只做核心體驗，**不超過 2 個頁面**
2. Sammy 親自試用 → 確認「感覺對了」
3. 截圖 + `git tag v0.1` — **設計基準線**
4. 寫 `DESIGN_ANCHOR.md` — 記錄不能動的設計元素

## Phase 2：迭代（每次只加一個功能）

1. 提案：功能加在哪？影響什麼？
2. **Sammy 同意才開工**
3. Spec 裡寫死「不能改的東西」
4. 開 git branch 做
5. 做完 → Sammy 對照 v0.1 截圖 → 初衷還在嗎？
6. OK → merge + tag

## Phase 3：品質把關（自動循環）

1. 領域專家 QA → < 7 分 → PO 寫 spec → Claude Coder 修 → 再 QA
2. UI/UX 顧問 → < 8 分 → 前端工程師修 → 再評
3. **任何「新增功能」建議 → 先問 Sammy**
4. QA/VC 是找 bug 和評分的，不決定產品方向

## Phase 4：商業驗證

1. VC review 商業價值
2. 找真實用戶測試
3. 根據數據決定下一步

---

## 🚨 鐵律

1. **QA 和 VC 是顧問，Sammy 是老闆**
2. **一次一功能** — 做完驗收通過才做下一個
3. **每次改完 git commit** — 沒 commit 等於沒做
4. **設計基準線不可侵犯** — 要改佈局先問 Sammy
5. **做之前先說「不做什麼」** — 防止 feature creep

---

## 教訓來源

Phonics Lab v0.1→v0.4：
- 原本 2 tab + 彩色音節卡片的美麗設計
- 三輪迭代後膨脹成 5 tab + onboarding + 挑戰 + 家族 + Phase 標籤
- QA 說缺功能就加、VC 說要 retention 就加，沒人守住設計初衷
- 沒有 git history，改壞了回不去
