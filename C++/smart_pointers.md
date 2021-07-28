# Smart Pointers

Defining
```
std::shared_ptr<TEMPLATE::TYPE> entity;
```

Instantiating:

```
std::make_shared<TEMPLATE::TYPE>(constructor_args);
```

Converting smart pointers:
```
entity.reset($SMART_POINTER)
```

Converting raw to smart pointer:
```
entity.reset($RAW_POINTER)
```

If any function have a raw pointer argument, e.g. ```function(TYPE *_m)```, just:

```
function(entity.get())
```
