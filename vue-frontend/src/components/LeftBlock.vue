<template>
    <div class="left-block">
        <div class="left-block-wrapper">
            <div class="answer-container">
                <div class="answer-container__header">
                    <span class="answer-container__header-text">Профиль клиента</span>
                </div>
                <ul class="answer-container__list">
                    <li class="answer-container__list-item">
                        <Multiselect
                            class="answer-container__list-item__input w-100 multiselect-blue"
                            v-model="values.sex"
                            mode="tags"
                            placeholder="Пол"
                            :options="options.sex"
                        />
                    </li>
                    <li class="answer-container__list-item">
                        <Multiselect
                            class="answer-container__list-item__input w-100 multiselect-blue"
                            v-model="values.age"
                            mode="tags"
                            placeholder="Возраст"
                            :options="options.age"
                        />
                    </li>
                    <li class="answer-container__list-item">
                        <Multiselect
                            class="answer-container__list-item__input w-100 multiselect-blue"
                            v-model="values.interest"
                            mode="tags"
                            placeholder="Интересы"
                            :options="options.interest"
                        />
                    </li>
                    <li class="answer-container__list-item">
                        <Multiselect
                            class="answer-container__list-item__input w-100 multiselect-blue"
                            v-model="values.cash"
                            mode="tags"
                            placeholder="Уровень дохода"
                            :options="options.cash"
                        />
                    </li>
                </ul>
            </div>
            <div class="button-container">
                <button
                    type="button"
                    class="btn btn-success w-100 start-search-button"
                    @click="apllyFilters()"
                >
                    Найти
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import Multiselect from '@vueform/multiselect'
import axios from 'axios';

export default {
  name: 'LeftBlock',
  components: {
    Multiselect,
  },
  methods: {
    apllyFilters () {
        this.$store.state.values = this.values
        console.log(JSON.stringify(this.values));

        axios.post(`http://10.0.36.11:1111/nostradamus/`,
        JSON.stringify(this.values),
        {
            headers: {
                'Content-Type': 'application/json'
            },
            auth: {
                username: 'lobanov',
                password: 'ivan'
            }
        })
        .then(response => {
            // this.$store.state.response = response.data
            console.log(response.data);
            for (var prop in response.data){
                for (var key in response.data[prop]){
                    console.log(key);
                }
            }
            console.log('request complete');
            this.$root.$emit('getResponse')
        })
        .catch(e => {
          this.errors.push(e)
        })
    }
  },
  computed: {
    //   isDisabled () {
    //     //   this.values.forEach(el=>{
    //     //       console.log(el);
    //     //   })
    //     var count = 0
    //     for (var prop in this.values) {
    //         console.log(this.values[prop])
    //         if (this.values[prop] == null){
    //             count = count + 1
    //         }
    //     }
    //     var result = Object.keys(this.values).length == count ? false : true

    //     return result
    //   }
  },
  data() {
    return {
      values: {
          sex: null,
          age: null,
          interest: null,
          cash: null,
      },
      options: {
        sex: [
          'м',
          'ж',
        ],
        age: [
          '0-18',
          '18-24',
          '25-34',
          '35-44',
          '45-54',
          '55-100',
        ],
        interest: [
          'Финансы и инвестиции',
          'Кафе, доставки',
          'Автолюбители',
        ],
        cash: [
          '0-20',
          '21-50',
          '51-100',
          '101-200',
        ]
      }
    }
  }
}
</script>

<style src="@vueform/multiselect/themes/default.css"></style>

<style scoped>
.multiselect-blue {
  --ms-tag-bg: #014c98;
  --ms-tag-color: #fff;
  --ms-tag-opacity: 0.7;
}
.left-block-wrapper {
    background-color: #fff;
    padding: 5px 20px 20px 20px;
    border-radius: 10px;
}
.answer-container__list {
    margin: 0;
    padding: 0;
}
.answer-container__header{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 40px;
}
.answer-container__list-item{
    list-style-type: none;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    /* height: 40px; */
    margin-top: 10px;
    border-radius: 10px;
    background-color: #F5F5F5;
}
.answer-container__list-item__input{
    /* height: 40px; */
    border-radius: 10px;
    background-color: #F5F5F5;
    /* padding-left: 15px; */
}
.start-search-button{
    margin-top: 10px;
}
</style>