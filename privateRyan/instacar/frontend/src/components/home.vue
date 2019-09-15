<template>
  <div class="home">
    <h1>{{msg1}}</h1>
    <h3>{{msg3}}</h3>
    <button type="button" class="btn btn-primary btn-lg btn-block" v-on:click="gotorideBook">{{msg2}}</button>
    <div class="row">
      <div class="col-md-4 col-lg4" v-for="(product) in products" :key="product.pk">
        <img v-bind:src= "require('../assets/'+product.fields.pics)" alt="" class="img-fluid" />
         <h3 @click="goTodetail(product.pk)"> {{product.fields.name}}</h3>
      </div>
    </div>
  </div>

</template>
<script>
import axios from "axios";
export default {
  name: "home",
  data() {
    return { 
      msg1: "THE CARS WE PROVIDE",
      msg2: "Let's Ride",
      msg3: "click on car's names to get details",
      products:[],
      errors: []
     };
  },
  methods:{
  goTodetail(prodId) {
    let proId=prodId
    this.$router.push({name:'details',params:{Pid:proId}})
  },
  gotorideBook(){
    this.$router.push({name:'trip'})
  }
  },
  mounted() {
    axios
      .get(`http://localhost:8000/onlyCars`)
      .then(response => {
        this.products = response.data;
      })
      .catch(e => {
        this.errors.push(e);
      });
  }
};
</script>
<style scoped>
.row img{
  max-height: 15em;
  width: 100%;

}
.row h3{
  cursor:pointer;
}
</style>