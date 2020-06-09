<template>
    <div>
        <div class="row">
            <div class="col">
                <div class="form-group">
                    <select v-model="selected_country" class="form-control">
                        <option value="">--- Select a country ---</option>
                        <option v-for="(data, key) in covid_data " :key="key" :value="key">{{ data['Country,Other'] }}</option>
                    </select>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col" v-if="selected_country !== ''">
                <h1>{{ covid_data[selected_country]['Country,Other'] }}</h1>
            </div>
        </div>
        <div v-if="selected_country !== ''" class="table-responsive">
            <table class="table">
                <tr>
                    <th>Total Cases</th>
                    <td>{{ covid_data[selected_country]['TotalCases'] }}</td>
                </tr>
                <tr>
                    <th>New Cases</th>
                    <td>{{ covid_data[selected_country]['NewCases'] }}</td>
                </tr>
                <tr>
                    <th>Total Deaths</th>
                    <td>{{ covid_data[selected_country]['TotalDeaths'] }}</td>
                </tr>
                <tr>
                    <th>New Cases</th>
                    <td>{{ covid_data[selected_country]['NewDeaths'] }}</td>
                </tr>
                <tr>
                    <th>Total Recovered</th>
                    <td>{{ covid_data[selected_country]['TotalRecovered'] }}</td>
                </tr>
                <tr>
                    <th>New Recovered</th>
                    <td>{{ covid_data[selected_country]['NewRecovered'] }}</td>
                </tr>
                <tr>
                    <th>Active Cases</th>
                    <td>{{ covid_data[selected_country]['ActiveCases'] }}</td>
                </tr>
                <tr>
                    <th>Critical Cases</th>
                    <td>{{ covid_data[selected_country]['Serious,Critical'] }}</td>
                </tr>
                <tr>
                    <th>Total Tests</th>
                    <td>{{ covid_data[selected_country]['TotalTests'] }}</td>
                </tr>
                <tr>
                    <th>Total Cases per 1M population</th>
                    <td>{{ covid_data[selected_country]['Tot\u00a0Cases/1M pop'] }}</td>
                </tr>
                <tr>
                    <th>Deaths per 1M population</th>
                    <td>{{ covid_data[selected_country]['Deaths/1M pop'] }}</td>
                </tr>
                <tr>
                    <th>Tests per 1M population</th>
                    <td>{{ covid_data[selected_country]['Tests\/\n1M pop\n'] }}</td>
                </tr>
            </table>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'CountryStats',

        data: function() {
            return {
                selected_country: '',
                covid_data: {}
            }
        },

        methods: {
            fetchData() {
                axios.get('/covid19.json').then(resp => {
                    this.covid_data = resp.data;
                })
                .catch(e => {
                    console.log(e);
                })
            },
        },

        created() {
            this.fetchData();
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
