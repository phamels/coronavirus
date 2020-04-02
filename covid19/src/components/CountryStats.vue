<template>
    <div>
        <div class="row">
            <div class="col">
                <div class="form-group">
                    <select v-model="selected_country" class="form-control">
                        <option value="">--- Select a country ---</option>
                        <option v-for="(data, country) in covid_data " :key="country">{{ country }}</option>
                    </select>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <h1>{{ selected_country }}</h1>
            </div>
        </div>
        <div v-if="selected_country !== ''" class="table-responsive">
            <table class="table">
                <tr>
                    <th>Total Cases</th>
                    <td>{{ covid_data[selected_country]['Total Cases'] }}</td>
                </tr>
                <tr>
                    <th>New Cases</th>
                    <td>{{ covid_data[selected_country]['New Cases'] }}</td>
                </tr>
                <tr>
                    <th>Total Deaths</th>
                    <td>{{ covid_data[selected_country]['Total Deaths'] }}</td>
                </tr>
                <tr>
                    <th>New Cases</th>
                    <td>{{ covid_data[selected_country]['New Deaths'] }}</td>
                </tr>
                <tr>
                    <th>Total Recovered</th>
                    <td>{{ covid_data[selected_country]['Total Recovered'] }}</td>
                </tr>
                <tr>
                    <th>Active Cases</th>
                    <td>{{ covid_data[selected_country]['Active Cases'] }}</td>
                </tr>
                <tr>
                    <th>Critical Cases</th>
                    <td>{{ covid_data[selected_country]['Critical Cases'] }}</td>
                </tr>
                <tr>
                    <th>Total Cases per 1M population</th>
                    <td>{{ covid_data[selected_country]['Tot Cases/1M pop'] }}</td>
                </tr>
                <tr>
                    <th>Deaths per 1M population</th>
                    <td>{{ covid_data[selected_country]['Deaths/1M pop'] }}</td>
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
