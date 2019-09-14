<template>
  <div class="home">
    <h1>{{msg1}}</h1>
    <h3>{{msg3}}</h3>
    <button type="button" class="btn btn-primary btn-lg btn-block" v-on:click="gotorideBook">{{msg2}}</button>
    <div class="row">
      <div class="col-md-4 col-lg4" v-for="(data,index) in products" :key="index">
        <img :src="data.image" class="img-fluid">
         <h3 @click="goTodetail(data.productId)"> {{data.productTitle}}</h3>
      </div>
    </div>
  </div>

</template>
<script>
export default {
  name: "home",
  data() {
    return { 
      msg1: "THE CARS WE PROVIDE",
      msg2: "Let's Ride",
      msg3: "click on cars' names to get details",
      products:[
      {
        productTitle:"AUDI",
        image       : require('../assets/Audi.jpg'),
        productId:1
      },
      {
        productTitle:"BENTLEY",
        image       : require('../assets/bentley.jpg'),
        productId:2
      },
      {
        productTitle:"FERRARI",
        image       : require('../assets/ferrari.jpg'),
        productId:3
      },
      {
        productTitle:"MERC",
        image       : require('../assets/Merc.jpg'),
        productId:4
      },
      {
        productTitle:"ROVER",
        image       : require('../assets/RangeRover.jpg'),
        productId:5
      },
      {
        productTitle:"TOYOTA",
        image       : require('../assets/Thar.jpg'),
        productId:6
      }
      ]
    }
  },
  methods:{
  goTodetail(prodId) {
    let proId=prodId
    this.$router.push({name:'details',params:{Pid:proId}})
  },
  gotorideBook(){
    this.$router.push({name:'blog'})
  }
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