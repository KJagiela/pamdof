<script setup>

import IngredientAdd from 'components/IngredientAdd.vue'

import { ref, reactive } from 'vue'

const name = ref('')
const originalUrl = ref('')
const instructions = ref('')

const ingredients = reactive([])

function submit () {
  console.log(name.value, originalUrl, instructions, ingredients[0])
}

</script>

<template>
  <q-page class="q-pa-lg">
    <q-form @submit="submit">
      <q-input
        v-model="name"
        label="Name"
        lazy-rules
        :rules="[val => !!val || 'Required']"
      />
      <q-input
        v-model="originalUrl"
        label="Original URL"
      />
      <q-input
        v-model="instructions"
        label="Instructions"
        type="textarea"
        lazy-rules
        :rules="[val => !!val || 'Required']"
      />
      <IngredientAdd v-for="(ingredient, index) in ingredients" :key="index" v-model="ingredients[index]"/>
      <q-btn icon="add" @click="ingredients.push({})" />
      <q-btn
        type="submit"
        label="Submit"
        color="primary"
        class="q-mt-md"
      />
    </q-form>
  </q-page>
</template>

<style scoped>

</style>
