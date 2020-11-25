# SpringBoot

## 概要

- springドキュメント
https://spring.pleiades.io/

- アプリケーションプロパティ
https://spring.pleiades.io/spring-boot/docs/current/reference/html/appendix-application-properties.html#transaction-properties

【参考】
- Spring Boot で簡単RESTful APIを作成する
https://qiita.com/L_A_P_119611/items/e44367ab6336f2fd09ea

MVC ⇒ Model,View,Controller

REAT APIに必要な要素

- データアクセスモデル
- リポジトリインタフェース
- Restコントローラー


```properties:/src/main/resources/application.properties
spring.datasource.driver-class-name=org.postgresql.Driver
spring.datasource.url=jdbc:postgresql://localhost:5432/testdb
spring.datasource.username=postgres
spring.datasource.password=hogehoge
```