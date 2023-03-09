# A second vue component.

<script>
export default {
  props: ["parentSliderValue"],
  data() {
    return {
      sliderValue: "",
      styles: { myDiv: {
        border: "5px outset red",
        backgroundColor: "lightblue",
        textAlign: "center"
    }}
    };
  },
};
</script>

<template>
  <v-card>
    <v-slider  v-model="sliderValue"  min=1 max=100></v-slider>
    <v-btn class="success_button">A</v-btn>
    <v-btn color="warning">text</v-btn>
    <p class="greeting">The parent slider is {{ parentSliderValue }},
       while this components slider is at {{ sliderValue }}</p>

  <div :style="styles.myDiv">
  <p>This is a styled component.</p>
</div>
</v-card>
</template>

<style>

</style>
