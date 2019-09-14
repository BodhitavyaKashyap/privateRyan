<template>
  <div class="details">
    <div class="container">
      <div class="row">
        <div class="col-md-12" v-for="(product,index) in products" :key="index">
          <div v-if="proId == product.productId">
              <h3>{{msg}}{{product.productTitle}}</h3>
            <img :src="product.image" class="img-fluid" />
            
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "details",
 
  data() {
    return {
      proId: this.$route.params.Pid,
      title: "details",
       msg:  "Details of ",
      products: [
        {
          productTitle: "AUDI",
          image: require("../assets/Audi.jpg"),
          productId: 1
        },
        {
          productTitle: "BENTLEY",
          image: require("../assets/bentley.jpg"),
          productId: 2
        },
        {
          productTitle: "FERRARI",
          image: require("../assets/ferrari.jpg"),
          productId: 3
        },
        {
          productTitle: "MERC",
          image: require("../assets/Merc.jpg"),
          productId: 4
        },
        {
          productTitle: "ROVER",
          image: require("../assets/RangeRover.jpg"),
          productId: 5
        },
        {
          productTitle: "TOYOTA",
          image: require("../assets/Thar.jpg"),
          productId: 6
        }
      ]
    };
  }
};
</script>