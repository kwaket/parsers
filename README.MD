# "Пауки" для сбора вакансий


## Запуск
1. В файл urls.txt добавить ссылки на страницу поиска вакансий, например
  `https://hh.ru/search/vacancy?text=data+engineer&search_field=name`
2. Запустить scrapy
  ```shell
  scrapy crawl hh -o $(date +%Y-%m-%d).csv -a "urls-file=urls.txt" -a "pages_num=15"
  ```
