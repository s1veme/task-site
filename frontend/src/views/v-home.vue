<template>
  <div class="v-home">
    <div
      class="h-screen relative"
      :style="{
        backgroundImage: `url(${require('@/assets/img/header-bg.jpg')})`,
        backgroundRepeat: 'no-repeat',
        backgroundSize: 'cover',
      }"
    >
      <div class="container mx-auto px-4 lg:px-16">
        <header>
          <ul
            class="list-none flex justify-around text-white pt-5 font-custom not-italic text-sm"
          >
            <li>Обучение</li>
            <li>Пройти квест</li>
            <li>История</li>
            <li>Обратиться</li>
            <li>Лидеры</li>
            <li>Личный кабинет</li>
            <router-link to="/login">Регистрация</router-link>
          </ul>
        </header>
        <section class="flex flex-warp">
          <div class="absolute top-45 ">
            <div class="font-custom text-white">
              <h1
                class="text-7xl font-black shadow-2xl lg:text-5xl"
                style="text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 4px 4px rgba(0, 0, 0, 0.25);"
              >
                Проект neCicada
              </h1>
              <p class="max-w-xl text-lg pt-5 lg:pt-3 lg:max-w-lg lg:text-base">
                Lorem ipsum dolor sit, amet consectetur adipisicing elit. Fugiat
                dolorem quod quae hic ducimus eos nam beatae velit possimus
                reiciendis, cupiditate quidem! Maiores laborum, quasi nesciunt
                obcaecati voluptate minima ullam.
              </p>
              <button
                class="focus:outline-none mt-7 px-16 py-4 bg-gradient-to-r from-purple-400 via-pink-500 to-red-500 font-custom font-black text-xl lg:text-lg lg:px-10 lg:py-3"
              >
                Испытать себя
              </button>
            </div>
          </div>
        </section>
      </div>
    </div>
    <hr />
    <section>
      <div
        :style="{
          backgroundImage: `url(${require('@/assets/img/who-bg.jpg')})`,
        }"
      >
        <div class="container mx-auto px-4 pt-6 lg:px-16">
          <h2
            class="text-white text-center font-black font-custom text-3xl"
            style="text-shadow: 7px 0px 1px #B100EF;"
          >
            Что здесь есть
          </h2>

          <div
            class="flex flex-wrap flex-row justify-between text-white items-center self-center"
          >
            <div class="flex pb-10 mt-7">
              <div class="w-2/6">
                <img :src="require('@/assets/img/who-icons/training.png')" />
              </div>
              <div class="self-center">
                <h3 class="text-2xl font-black">Обучение</h3>
                <p class="text-lg">Туториал по прохождению</p>
              </div>
            </div>
            <div class="flex pb-10  mt-7">
              <div class="w-2/6">
                <img :src="require('@/assets/img/who-icons/brain.png')" />
              </div>
              <div class="self-center">
                <h3 class="text-2xl font-black">Обучение</h3>
                <p class="text-lg">Туториал по прохождению</p>
              </div>
            </div>
            <div class="flex pb-10  mt-7">
              <div class="w-2/6">
                <img :src="require('@/assets/img/who-icons/book.png')" />
              </div>
              <div class="self-center">
                <h3 class="text-2xl font-black">Обучение</h3>
                <p class="text-lg">Туториал по прохождению</p>
              </div>
            </div>
            <div class="flex">
              <div class="w-2/6">
                <img :src="require('@/assets/img/who-icons/notebook.png')" />
              </div>
              <div class="self-center">
                <h3 class="text-2xl font-black">Обучение</h3>
                <p class="text-lg">Туториал по прохождению</p>
              </div>
            </div>
            <div class="flex">
              <div class="w-2/6">
                <img :src="require('@/assets/img/who-icons/liders.png')" />
              </div>
              <div class="self-center">
                <h3 class="text-2xl font-black">Обучение</h3>
                <p class="text-lg">Туториал по прохождению</p>
              </div>
            </div>
            <div class="flex">
              <div class="w-2/6">
                <img :src="require('@/assets/img/who-icons/account.png')" />
              </div>
              <div class="self-center">
                <h3 class="text-2xl font-black">Обучение</h3>
                <p class="text-lg">Туториал по прохождению</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div
        :style="{
          backgroundImage: `url(${require('@/assets/img/cicada-bg.jpg')})`,
          backgroundRepeat: 'no-repeat',
          backgroundSize: 'cover',
        }"
      >
        <div class="container mx-auto py-20 lg:px-16">
          <div class="text-white font-custom ">
            <p class="text-lg font-normal not-italic">
              Предмет нашего вдохновения
            </p>
            <h2 class="text-4xl font-black lg:text-3xl">
              Таинственная загадка Cicada3301
            </h2>
            <p class="text-lg pt-5 max-w-10xl lg:pt-3">
              Привет. Мы ищем лиц с высоким интеллектом. Для этого мы
              разработали тест. В этом изображении есть скрытое сообщение.
              Найдите его, и оно покажет вам, как найти нас. С нетерпением ждем
              тех немногих, кому удастся пройти весь путь. Удачи. 3301... Такое
              сообщение увидели пользователи...
            </p>
          </div>
          <button
            class="focus:outline-none mt-10 px-12 py-3 bg-gradient-to-r from-purple-400 via-pink-500 to-red-500 font-custom font-black text-lg text-white lg:py-2 lg:px-10 lg:mt-"
          >
            Узнать подробнее
          </button>
        </div>
      </div>
    </section>
    <hr />
    <section class="bg-indigo-800">
      <div class="container mx-auto px-4 py-4 lg:px-16">
        <h2
          class="text-white text-center font-black font-custom text-3xl pt-8"
          style="text-shadow: 7px 0px 1px #B100EF;"
        >
          Кто мы такие?
        </h2>

        <div class="flex justify-around mt-16">
          <div class="">
            <img :src="require('@/assets/img/who-we/1.png')" />
          </div>
          <div class="text-right self-center text-white">
            <p class="text-xl font-custom max-w-2xl lg:max-w-3xl">
              Далеко-далеко за словесными горами в стране гласных и согласных,
              живут рыбные тексты. Вершину вопрос на берегу путь приставка
              текста напоивший, безопасную последний? Не использовало на берегу
              агентство ты свою жизни даль текст продолжил даже!
            </p>
          </div>
        </div>
      </div>
    </section>
    <hr />
    <section>
      <div
        :style="{
          backgroundImage: `url(${require('@/assets/img/bg-questions.jpg')})`,
          backgroundRepeat: 'no-repeat',
          backgroundSize: 'cover',
        }"
      >
        <div
          class="container mx-auto px-4 pt-16 text-center font-custom text-white "
        >
          <h2 class=" text-3xl font-black">
            Есть вопросы?
          </h2>
          <div class="text-center mx-auto max-w-4xl">
            <p class="text-lg pt-6">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
              enim ad minim veniam, quis nostrud exercitation ullamco laboris
              nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
              reprehenderit in
            </p>
          </div>

          <form action="POST" class="py-10">
            <input
              type="text"
              placeholder="Ваш email"
              class="block mx-auto w-3/6 py-3 pl-2 text-black focus:outline-none"
            />
            <textarea
              placeholder="Ваше сообщение"
              class="block mx-auto mt-6 w-3/6 py-6 pl-2 text-black focus:outline-none"
            ></textarea>
          </form>
        </div>
      </div>
    </section>
    <hr />
    <footer>
      <div class="bg-indigo-900">
        <div class="container mx-auto px-4 pt-10">
          <div class="flex justify-around font-custom text-white text-xl">
            <div>
              <h4 class="border-b-2 border-white pb-1 font-black">Контакты</h4>
              <ul class="pt-2">
                <li>
                  <a href="#">Email</a>
                </li>
                <li>
                  <a href="#">Telegram</a>
                </li>
              </ul>
            </div>
            <div>
              <h4 class="border-b-2 border-white pb-1 font-black">Контакты</h4>
              <ul class="pt-2">
                <li>
                  <a href="#">Email</a>
                </li>
                <li>
                  <a href="#">Telegram</a>
                </li>
              </ul>
            </div>
            <div>
              <h4 class="border-b-2 border-white pb-1 font-black">Контакты</h4>
              <ul class="pt-2">
                <li>
                  <a href="#">Email</a>
                </li>
                <li>
                  <a href="#">Telegram</a>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="bg-black text-center font-custom text-white mt-16 py-4">
          <p>neCicada - неЦикада. Апрель 2077г.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: "v-home",

  data() {
    return {};
  },
};
</script>

<style scoped>
hr {
  position: absolute;
  width: 100%;
  border: 6px solid #ff00c8;
  color: black;
  border-radius: 2px;
  box-shadow: 100px 100px 100px #ff00c8;
  padding: 0;
  animation: glow 1.5s ease-in-out infinite;
  -webkit-animation: glow 1.5s ease-in-out infinite;
}

@keyframes glow {
  0% {
    box-shadow: 0 0 2px red;
  }
  50% {
    box-shadow: 0 0 8px red;
  }
  100% {
    box-shadow: 0 0 2px red;
  }
}

@-webkit-keyframes glow {
  0% {
    box-shadow: 0 0 2px red;
  }
  50% {
    box-shadow: 0 0 8px red;
  }
  100% {
    box-shadow: 0 0 2px red;
  }
}

@keyframes glowMinor {
  0% {
    box-shadow: 0 0 2px black;
  }
  50% {
    box-shadow: 0 0 8px black;
  }
  100% {
    box-shadow: 0 0 2px black;
  }
}

@-webkit-keyframes glowMinor {
  0% {
    box-shadow: 0 0 2px black;
  }
  50% {
    box-shadow: 0 0 8px black;
  }
  100% {
    box-shadow: 0 0 2px black;
  }
}
</style>
