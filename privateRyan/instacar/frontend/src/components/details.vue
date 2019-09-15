<template>
  <div class="details">
    <div class="container">
      <div class="row">
        <div class="col-md-12" v-for="(product) in products" :key="product.pk">
          <div v-if="proId == product.pk">
            <h3>{{msg}} {{product.fields.name}}</h3>
            <h3>{{msg1}} {{product.fields.description}}</h3>
            <img v-bind:src= "require('../assets/'+product.fields.pics)" alt="" class="img-fluid" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "details",
  data() {
    return {
      proId: Number(this.$route.params.Pid),
      title: "details",
      msg: "Details of ",
      msg1: "Features: ",
      products: [],
      errors: []
    };
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