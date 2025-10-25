 <div id="top" align="center">

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

</div>

<br />
<h3 align="center"> 🪴 Prayer Garden Backend API 🪴 </h3>

  <p align="center">
    REST API for prayer garden!
  </p>
    <br />
    <a href="#"><strong>Explore the docs »</strong></a>
    <br />
    <br />
<a href="https://github.com/SharleneNdinda/prayer-garden/issues">Report Bug</a>
·
    <a href="https://github.com/SharleneNdinda/prayer-garden/issues">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## 🚀 About The Project

Prayer garden is a cute, functional application. It is meant to deliver the following:

    ✅ Be able to pick a prayer focus from a list of options.

### Built With

![Django][Django]


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🚀 Getting Started

1. Clone this repository and setup virtual environment. Install all project requirements before proceeding.

```sh
  $ pip install -r requirements/base.txt
```

2. Setup your local `Postgres` database, update database configs and run migrations.

```sh
  $ python manage.py migrate
```

3. Run development server.

```sh
  $ python manage.py runserver
```

## 🚀 Usage

### 🥠 API Endpoints

| Endpoint | URL                 | Description         | 
| -------- | ------------------- | ------------------- |
| Prayer Classifications    | /api/prayer/prayer_classifications/    | Display prayer classifications         | 




[contributors-shield]: https://img.shields.io/github/contributors/SharleneNdinda/prayer-garden?style=for-the-badge
[contributors-url]: https://github.com/SharleneNdinda/prayer-garden/contributors
[forks-shield]: https://img.shields.io/github/forks/SharleneNdinda/prayer-garden?style=for-the-badge
[forks-url]: https://github.com/SharleneNdinda/prayer-garden/forks
[stars-shield]: https://img.shields.io/github/stars/SharleneNdinda/prayer-garden?style=for-the-badge
[stars-url]: https://github.com/SharleneNdinda/prayer-garden/stargazers
[issues-shield]: https://img.shields.io/github/issues/SharleneNdinda/prayer-garden?style=for-the-badge
[issues-url]: https://github.com/SharleneNdinda/prayer-garden/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: in/sharlene-mutuku-86571518b
[product-screenshot]: images/architecture.png
[x-ray-trace]: images/trace.png
[Django]: https://img.shields.io/badge/django-35495E?style=for-the-badge&logo=django&logoColor=87CEEB
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
