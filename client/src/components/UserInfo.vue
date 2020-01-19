<template>
    <div class="userInfo"> 
        <span class="name">
            Welcome, Huyen Pham!
        </span>
        <span class="major">
            Computer Science, B.S.
        </span>
    </div>
    
</template>

<script>
export default {
    name: 'UserInfo'
}

</script>

<style scoped>
.userInfo {
    font-size: 20px;
    height: 50px;
    display: flex;
    justify-content: space-between;
    margin: 0 200px;
}

.name {
    align-self: center;
    font-weight: bold;
}

.school {
    align-self: center;
}

.major {
    align-self: center;
}


</style>