<template>
  <div class="blog">
    <h1>{{title}}</h1>
    <form action="http://localhost:8000/cars" method="POST">
      <fieldset>
        <fieldset class="form-group">
          <legend>Select trip type</legend>
          <div class="form-check">
            <label class="form-check-label">
              <input
                type="radio"
                class="form-check-input"
                name="tripType"
                id="optionsRadios1"
                value="RoudTrip"
                checked
                v-model="triptype"
              />
              Round Trip
            </label>
          </div>
          <div class="form-check">
            <label class="form-check-label">
              <input
                type="radio"
                class="form-check-input"
                name="tripType"
                id="optionsRadios2"
                value="OneWay"
                v-model="triptype"
              />
              One Way
            </label>
          </div>
        </fieldset>
        <div class="form-group">
          <label for="exampleSelect1">Select Destination</label>
          <select class="form-control" id="exampleSelect1" v-model="destination" name="destination">
            <option v-for="option in options" :key="option.pk">{{ option.fields.city }}</option>
          </select>
        </div>
        <div class="form-group">
          <label for="exampleSelect1">Select Start Date</label>
          <datepicker style="text-align:center ;" name="startDate" v-model="startdate"></datepicker>
        </div>
        <div class="form-group">
          <label for="exampleSelect1">Select End Date</label>
          <datepicker style="text-align:center ;" name="endDate" v-model="enddate"></datepicker>
        </div>
        <button  class="btn btn-primary" v-on:click="next2">next</button>
        <button  type="submit" class="btn btn-primary" >next1</button>
      </fieldset>
    </form>
  </div>
</template>
<script>
import Datepicker from "vuejs-datepicker";
import axios from "axios";
export default {
  name: "trip",
  data() {
    return {
      title: "START TRIPPING ",
      options: [],
      destination: "",
      startdate: "",
      enddate: "",
      triptype: ""
    };
  },
  components: {
    Datepicker
  },
  mounted() {
    axios
      .get(`http://localhost:8000/destinations`)
      .then(response => {
        //console.log(response.data)
        this.options = response.data;
        //console.log(options)
      })
      .catch(e => {
        this.errors.push(e);
      });
  },
  methods: {
    next2() {
        //console.log("hijjjjjjjjjjjjjjjhgfdesdfghjhgfrdesdcfghjnbvfcdszxcvghnbvcxszxcvh")
      let currentObj = this;
      this.axios
        .post('http://localhost:8000/cars', {params:{
          "destination": this.destination,
          "start_date": this.startdate,
          "end_date":this.enddate,
          "trip_type":this.triptype
        }})
        .then(function(response) {
          currentObj.output = response.data;
          //this.$router.push({name:'blog'})
        })
        .catch(function(error) {
          currentObj.output = error;
        });
    }
  }
};
</script>
<style scoped>
</style>