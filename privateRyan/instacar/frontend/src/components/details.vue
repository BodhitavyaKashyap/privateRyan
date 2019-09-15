<template>
  <div class="details">
    <div class="container">
      <div class="row">
        <div class="col-md-12" v-for="product in products" :key="product.id">
          <div v-if="proId == product.id">
            <h3>{{msg}} "product.name"</h3>
            <h3>{{msg1}} "product.description"</h3>
            <img :src="product.pics" class="img-fluid" />
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
      msg1: "Features ",
      products: [],
      errors: []
    };
  },
  mounted() {
    axios
      .get(`http://localhost:8000/onlyCars`)
      .then(response => {
          console.log(response.data)
          let z=JSON.parse(response.data);
          console.log(z)
          json.forEach((z) => {
        console.log('ID: ' + z.name);
        console.log('MSG: ' + z.pics);
        console.log('TID: ' + z.id);
        console.log('FROMWHO: ' + z.description);
});
        this.products = JSON.parse(response.data);
      })
      .catch(e => {
        this.errors.push(e);
      });
  }
};
</script>