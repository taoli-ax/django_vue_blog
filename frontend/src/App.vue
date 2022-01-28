
<template>
    <div id="header">
        <h1>My django Vue blog</h1>
        <hr>
    </div>
    <div v-for="article in info.results" v-bind:key="article.url" id="articles">
        <div class="article-title">
            {{ article.title }}
        </div>
        <div>{{ formatted_time(article.created) }}</div>
    </div>
    <div id="footer">
        <p>rose-jack-taitanic.com</p>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'App',
        data: function () {
            return {
                info: ''
            }
        },
        mounted() {
            axios
                .get('/api/article')
                .then(response => (this.info = response.data))
        },
        methods:{
            formatted_time:function(iso_date_string){
                const date = new Date(iso_date_string);
                return date.toLocaleDateString()
            }
        }
    }
</script>

<style>
 #app {
        font-family: Georgia, Arial, sans-serif;
        margin-left: 40px;
        margin-right: 40px;
    }
    #articles {
        padding: 10px;
    }

    .article-title {
        font-size: large;
        font-weight: bolder;
        color: black;
        text-decoration: none;
        padding: 5px 0 5px 0;
    }
    #header{
        text-align: center;
        margin-top: 20px;
    }
    #footer{
        position:relative;
        left: 0;
        bottom: 0;
        height: 50px;
        widows: 100%;
        background: whitesmoke;
        text-align: center;
        font-weight: bold;
    }
</style>