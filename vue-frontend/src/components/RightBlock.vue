<template>
    <div class="right-block">
        <div class="right-block__top h-25">
            <div class="charts-container-wrapper h-100">
                <div class="row">
                    <div class="col-4">
                        <div class="age-container-chart">
                            <DoughnutChart
                            chart-title="Возраст"
                            :chart-labels="ages.chartLabels"
                            :background-color="ages.backgroundColor"
                            :datasets="ages.datasets"/>
                        </div>
                    </div>
                    <div class="col-4">
                        <div class="sex-container-chart">
                            <DoughnutChart
                            chart-title="Пол"
                            :chart-labels="sex.chartLabels"
                            :background-color="sex.backgroundColor"
                            :datasets="sex.datasets"/>
                        </div>
                    </div>
                    <div class="col-4">
                        <div class="cash-container-chart">
                            <DoughnutChart
                            chart-title="Уровень дохода"
                            :chart-labels="cash.chartLabels"
                            :background-color="cash.backgroundColor"
                            :datasets="cash.datasets"/>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="right-block__bottom h-75">
            <div class="groups-container h-100">
                <div class="groups-container-header">
                    <span class="group-container-header__text">
                        Площадки
                    </span>
                </div>
                <div class="groups-container-sites-wrapper">
                    <ul class="groups-container-sites">
                        <li class="group-container-site active">
                            <span class="group-container-site__text">
                                Вконтакте
                            </span>
                        </li>
                        <li class="group-container-site">
                            <span class="group-container-site__text">
                                Телеграм
                            </span>
                        </li>
                        <li class="group-container-site">
                            <span class="group-container-site__text">
                                Яндекс.Дзен
                            </span>
                        </li>
                        <li class="group-container-site">
                            <span class="group-container-site__text">
                                YouTube
                            </span>
                        </li>
                    </ul>
                </div>
                <div class="groups-container-info">
                    <!-- <ag-grid-vue
                        style="width: 100%; height: 200px"
                        :columnDefs="columnDefs"
                        :rowData="rowData"
                        >
                    </ag-grid-vue> -->
                    <table class="table">
                        <thead>
                            <tr>
                                <th scope="col">name</th>
                                <th scope="col">URL</th>
                                <th scope="col">Подписчики</th>
                                <th scope="col">Охват</th>
                                <th scope="col">Стоимость</th>
                                <th scope="col">Соответствие</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr @click="collapse1 = !collapse1" aria-controls="collapsibleContent1">
                                <th scope="row">Netflix</th>
                                <td>https://vk.com/tvnetflix</td>
                                <td>35000</td>
                                <td>1000</td>
                                <td>2500</td>
                                <td>74%</td>
                            </tr>
                                <tr>
                                    <td colspan="6">
                                        <MDBCollapse
                                            id="collapsibleContent1"
                                            v-model="collapse1"
                                        >
                                            <div class="collapsible-block">
                                                <div class="collapsible-block-header">
                                                    Статистика размещений
                                                </div>
                                                <div class="collapsible-block-middle">
                                                    <div class="collapsible-block-middle__images">
                                                        <img class="m-2" src="../assets/image1.png" alt="ural">
                                                        <img class="m-2" src="../assets/image2.png" alt="ural">
                                                        <img class="m-2" src="../assets/image3.png" alt="ural">
                                                    </div>
                                                    <div class="collapsible-block-middle__buttons">
                                                        <button
                                                            type="button"
                                                            class="btn btn-primary w-75 mt-4 m-2 pr-2 fill-report-button"
                                                            @click="apllyFilters()"
                                                        >
                                                            Заполнить отчет
                                                        </button>
                                                                        <button
                                                            type="button"
                                                            class="btn btn-success w-75 m-2 pr-2 download-report-button"
                                                            @click="apllyFilters()"
                                                        >
                                                            Выгрузить отчет
                                                        </button>
                                                    </div>
                                                </div>
                                                <div class="collapsible-block-table">
                                                    <table class="table">
                                                    <thead>
                                                        <tr>
                                                            <th scope="col">Публикация</th>
                                                            <th scope="col">Расходы</th>
                                                            <th scope="col">Клики</th>
                                                            <th scope="col">Покупки</th>
                                                            <th scope="col">CR</th>
                                                            <th scope="col">CPO</th>
                                                            <th scope="col">Доход</th>
                                                            <th scope="col">ROMI</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr>
                                                            <td>1. От 13.12.21</td>
                                                            <td>р.24 623</td>
                                                            <td>2433</td>
                                                            <td>50</td>
                                                            <td>2,14%</td>
                                                            <td>р.492,5</td>
                                                            <td>р.56 588</td>
                                                            <td>229,82%</td>
                                                        </tr>
                                                        <tr>
                                                            <td>2. От 15.01.22</td>
                                                            <td>р.10 702</td>
                                                            <td>431</td>
                                                            <td>37</td>
                                                            <td>8,58%</td>
                                                            <td>р.289,2</td>
                                                            <td>р.44 135</td>
                                                            <td>229,82%</td>
                                                        </tr>
                                                        <tr>
                                                            <td>3. От 26.01.22</td>
                                                            <td>р.10 285</td>
                                                            <td>604</td>
                                                            <td>21</td>
                                                            <td>3,48%</td>
                                                            <td>р.489,8</td>
                                                            <td>р.36 571</td>
                                                            <td>355,58%</td>
                                                        </tr>
                                                    </tbody>
                                                    <tfoot>
                                                        <tr>
                                                            <td>Итого</td>
                                                            <td>р.45 610</td>
                                                            <td>3368</td>
                                                            <td>108</td>
                                                            <td>3,21%</td>
                                                            <td>р.422,3</td>
                                                            <td>р.137 294</td>
                                                            <td>301,02%</td>
                                                        </tr>
                                                    </tfoot>
                                                    </table>
                                                </div>
                                            </div>
                                        </MDBCollapse>
                                    </td>
                                </tr>
                            <tr>
                                <th scope="row">Читающие</th>
                                <td>https://vk.com/tvnetflix</td>
                                <td>35000</td>
                                <td>1000</td>
                                <td>2500</td>
                                <td>74%</td>
                            </tr>
                            <tr>
                                <th scope="row">Импровизация</th>
                                <td>https://vk.com/tvnetflix</td>
                                <td>35000</td>
                                <td>1000</td>
                                <td>2500</td>
                                <td>74%</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import DoughnutChart from '@/components/doughnutChart.vue'
// import { AgGridVue } from "ag-grid-vue3";
import { MDBCollapse } from "mdb-vue-ui-kit"
import { ref } from 'vue';

import "ag-grid-community/dist/styles/ag-grid.css";
import "ag-grid-community/dist/styles/ag-theme-alpine.css";

export default {
    name: 'RightBlock',
    // props: {
    //   collapse1: {
    //     type: Boolean,
    //     default: false
    //   }
    // },
    components: {
        DoughnutChart,
        MDBCollapse
        // AgGridVue
    },
    methods: {

    },
    mounted() {
        console.log('in right component',this.$store.state.values);
        // this.$root.$on('getResponse', function (values) {
        //     console.log(values);
        // })
    },
    computed : {
        age() {
            console.log('111', this.$store.state.response);
            return 11
        }
    },
    data() {
        return {

            ages:{
                chartLabels: ['до 18', '18-24', '25-34', '35-44', '45-54', '55-100'],
                backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16', '#2D00F9', '#006426'],
                datasets: ['1640', '25218', '56869', '75790', '61377', '84988']
            },
            sex:{
                chartLabels: ['мужской', 'женский'],
                backgroundColor: ['#41B883', '#E46651'],
                datasets: ['171915', '199668']
            },
            cash:{
                chartLabels: ['0-20', '21-50', '51-100', '101-200'],
                backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
                datasets: ['1640', '25218', '56869', '75790']
            }

        }
    },
    setup() {
        const collapse1 = ref(false);

        return {
            collapse1,
        };
    },
}
</script>

<style scoped>
.right-block__bottom {
    padding: 10px 0 10px 0;
}
.charts-container-wrapper {
    border-radius : 10px;
    background: #fff;
    display: flex;
    justify-content : center;
    align-items : center;
}
.groups-container{
    border-radius: 10px;
    background-color: #fff;
}
.groups-container-header {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    height: 40px;
}
.group-container-header__text {
    padding-left: 15px;
}
.groups-container-sites {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    padding: 0;
    margin: 0;
    height: 40px;
}
.group-container-site {
    list-style-type: none;
    margin-left: 15px;
    background-color: #F5F5F5;
    border-radius: 5px;
    padding: 5px;
}
.group-container-site.active {
    background-color: rgb(1, 76, 152);
    opacity: 0.7;
    color: white;
}
.groups-container-info {
    margin-top: 10px;
    height: calc(100%-80px);
}
.collapsible-block-middle {
    display: flex;
}
.collapsible-block-middle__images {
    display: flex;
    padding: 5px;
}
.collapsible-block-middle__images {
    display: flex;
    padding: 5px;

}
</style>
