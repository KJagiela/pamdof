<script setup>
import { ref } from 'vue'
import { api } from 'boot/axios'

const props = defineProps({
  modelValue: {
    type: Object,
    required: true
  }
})
defineEmits(['update:modelValue'])

const name = ref(props.modelValue.name || '')
const amount = ref(0)
const unit = ref('')

const units = ref([])
// TODO: use pinia
api.get('ingredients/units/').then((response) => {
  units.value = response.data
}).catch((error) => {
  console.log(error)
})

const ingredients = ref([])
api.get('ingredients/').then((response) => {
  ingredients.value = response.data

}).catch((error) => {
  console.log(error)
})

</script>

<template>
<div class="row">
  <q-select
    v-model="name"
    :options="ingredients"
    label="Name"
    lazy-rules
    :rules="[val => !!val || 'Required']"
    @update:model-value="$emit('update:modelValue', {name, amount, unit})"
  />
  <q-input
    type="number"
    v-model="amount"
    label="Amount"
    lazy-rules
    :rules="[val => !!val || 'Required']"
    @update:model-value="$emit('update:modelValue', {name, amount, unit})"
  />
  <q-select v-model="unit" :options="units" label="Unit"
    @update:model-value="$emit('update:modelValue', {name, amount, unit})"

  />
</div>
</template>

<style scoped>

</style>
