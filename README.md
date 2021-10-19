# Quizz

## Plateforme de Quizz

---

### Fonctionnalités

> Un user doit se connecter pour accéder aux questions
>
> Un user peut créer des questions et également y répondre
>
>Un user ne peut répondre qu’une seule fois à un quizz, lorsqu’il n’y a plus de questions, on lui propose d’ajouter des questions 
>
>On doit enregistrer:
>-Le score d’un user quand il répond aux questions
>-Le score du user  (meilleur créateur de questions)

--- 

### Contributing

**Pour bien démarrer**

Après avoir cloné, dans un venv : 
```bash 
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```