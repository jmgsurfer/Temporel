# ToDo:
- determiner os: os.name():'nt' ou 'posix'
  - mettre condition sur os.system('clear') ou os.system('cls') en fonction os.name
- specifier encodage pour les accents et autres (windows-1252 vs. UTF-8)
  - coding: UTF-8
  - attention dans les raw_input(), ne pas préfixé les strings avec accents avec u"string"
