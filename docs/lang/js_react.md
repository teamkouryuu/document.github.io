# reactの環境構築

※Windows10での環境構築

## 目次

- Node.jsのインストール
- npmの使い方
- react.jsのインストール

---

### Node.jsのインストール

Node.jsの公式サイト
[https://nodejs.org/ja/](https://nodejs.org/ja/)  

#### インストール手順

- [xx.xx.x LTS（推奨版）] ⇒ をクリックでインストーラーをDL
- DL後、インストーラー起動。  
- すべて「次へ(Next)」を選択しインストール  

#### インストール後の確認※コマンドプロンプトで確認  

- node.jsのバージョン確認  
  `node --version`または`node -v`を入力  

  ```bash
  C:\Users\PCUSER>node --version
  vxx.xx.x
  ```

- npmのバージョン確認  
  npmはjavascriptのpackageマネージャー  
  `npm --version`または`npm -v`を入力 ※バージョンが表示される

  ```bash
  C:\Users\PCUSER>npm --version
  x.xx.x
  ```

#### 【補足】npmコマンド

- `npm init` - 初期化(package.jsonの生成)  

    ```bash
    npm init

    …省略…

    package name: (react_sample)
    version: (1.0.0)
    description:
    entry point: (index.js)
    test command:
    git repository:
    keywords:
    author:
    license: (ISC)

    …省略…

    Is this OK? (yes)
    ```

- `npm install` - 一括パッケージインストール(package.json)  
- `npm install <package_name>` - パッケージインストール  
- `npm install -dev <package_name>` - パッケージインストール  
- `npm uninstall <package_name>` - アンインストール  

---

### React環境構築

- 作業用ディレクトリを作成  

  ```bash
  mkdir dev_react
  cd dev_react
  ```

- reactのアプリケーションを作成  

  ```bash
  npx create-react-app myapp  
  cd myapp
  ```

- アプリケーションサーバーの開始  

  ```bash
  npm start
  ```
