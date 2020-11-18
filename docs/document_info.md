# Mkdocsについて

このドキュメントはpythonのライブラリのmkdocsでできています。

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

### Pythonのコマンド一覧

### mkdocsのコマンド一覧
* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # ドキュメントのホーム.
               # Other markdown pages, images and other files.

- テーマ [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

- 拡張機能 [PyMdown](https://facelessuser.github.io/pymdown-extensions/)


## fdsa f
fdsa fds

```mermaid
    graph TB;
        c1-->a2
        subgraph one
        a1-->a2
        end
        subgraph two
        b1-->b2
        end
        subgraph three
        c1-->c2
        end
```

```{.python .extra-class linenums="1"}
import hello_world
```

```plantuml
@startuml
Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response

Alice -> Bob: Another authentication Request
Alice <-- Bob: another authentication Response
@enduml
```
