<template>
    <div class="term">
        <p class="termName">{{termName}}</p>
        <ul id="classList">
            <li v-for="elm in termClass" v-bind:key="elm">
                {{elm}}
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'Term',
    props: [
        'termName',
        'termClass'
    ]
}
</script>

<style scoped>
.term {
    background-color: rgb(241, 222, 181);
    width: 250px;
    height: 200px;
    margin: 20px;
    justify-self: center;
}

.newTerm {
    background-color: rgb(241, 222, 181);
    width: 250px;
    height: 200px;
    margin: 20px;
    justify-self: center;
}

p.termName {
    font-weight: bold;
    padding-top: 10px;
    font-size: 17px;
}

ul#classList {
    margin: 0 15px;
    list-style: none;
    padding: 0;
    text-align: left;
    font-size: 15px;
}

</style>