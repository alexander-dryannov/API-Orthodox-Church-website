# REST API для церковных сайтов

## Задачи

### Общие

- [ ] Добавить разрешения

### Галерея

#### Описание приложения "галерея"

Если не будут добавлены изображения, то создастся пустой альбом. Если изображения выбраны, то они загружаются, обрабатываются(в данном случае конвертируются в .webp и переименовываются), записываются на хост и записываются в БД путь до изображения.

- [x] Добавление отдельных фото
- [x] Редактирование отдельных фото
- [x] Удаление отдельных фото

### Расписание

#### Описание приложения "расписание"

Загружается .docx файл, парсится и записыватся в БД как JSON.

- [x] Модель
- [x] Админка
- [x] Сериализатор
- [x] Изменение расписания путем загрузки другого файла
- [x] Удаление расписания

### Блог

#### Описание приложения "блог"

Обычный блог.

- [ ] Модель
- [ ] Админка
- [ ] Сериализатор
- [ ] CRUD

### Духовенство

#### Описание приложения "духовенство"

Информация о духовенстве.

- [x] Модель
- [x] Админка
- [x] Сериализатор
- [x] CRUD
- [ ] Удаление старой фотографии при ее обновлении

### Пожертвования

#### Описание приложения "пожертвования"

Представляет собой набор реквизитов для перевода денежных средств.

- [x] Модель
- [x] Админка
- [x] Сериализатор
- [x] CRUD
