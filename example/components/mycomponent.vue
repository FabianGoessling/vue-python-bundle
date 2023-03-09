# A first vue component, which nests other vue components.

<script>
export default {
  props: [],
  data() {
    return {
      sliderValue: "",
      greeting: "Hello there!",
    };
  },
};
</script>

<template>
  <v-card>
    <v-slider v-model="sliderValue" min=1 max=100> </v-slider>
    <p class="greeting">{{ greeting }}, the slider above is at {{ sliderValue }}</p>
    <secondcomponent :parentSliderValue="sliderValue"></secondcomponent>
    <secondcomponent :parentSliderValue="sliderValue"></secondcomponent>
  </v-card>
</template>

<style>
.greeting {
  color: red;
  font-weight: bold;
}
</style>
