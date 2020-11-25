# REST API

REST APIついて、それぞれキーワードを『REST』と『API』に分けて解説

## APIついて

`API：Application Programming Interfaceの略`  
- 直訳すると、「アプリケーションをプログラミングするためのインターフェース」  
- インターフェースとは、ソフトウェア同志を繋ぐ役割を持つ  
- ソフトウェアやアプリケーションなどの一部を外部に向けて公開することで、  
  第三者が開発したソフトウェアと機能を共有できるようにしてくれるもの。  
    - 例）異なるサービス間で認証機能を有する

## RESTついて

`REST：Representational State Transferの略`  

### RESTとは設計原則
- RESTとはWEB技術を用いた **4つの設計原則**
- RESTの設計原則を用いてAPIに適用したインタフェースがREST APIと言われる
　　
### RESTの4つの設計原則

1. セッション等の状態管理を行わない
2. 情報を操作する命令の体系があらかじめ定義されている (HTTPのGETやPOSTなど)
3. 全ての情報は汎用的な構文で一意に識別される (URLやURIなど)  
4. 情報の内部に、別の情報やリンクを含めることができる  
・リソースに対してURLが対応づけられる


## まとめ  
- REST APIはクライアントとサーバー間のデータのやり取りで使われるインタフェースの一種


##### 参考資料  
- APIとは何か？をできる限りわかりやすく説明したい  
https://www.setouchino.cloud/blogs/80  
- REST  
https://www.atmarkit.co.jp/ait/articles/1601/13/news033.html  
