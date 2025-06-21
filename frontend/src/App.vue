<template>
  <div class="app">
    <h1>欢迎使用Vue 3前端应用</h1>
    <p>后端状态: {{ backendStatus }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      backendStatus: '未连接'
    }
  },
  async mounted() {
    try {
      const response = await fetch('http://localhost:8080/api/health')
      this.backendStatus = await response.text()
    } catch (error) {
      this.backendStatus = '连接失败'
    }
  }
}
</script>

<style>
.app {
  text-align: center;
  margin-top: 50px;
  font-family: Arial, sans-serif;
}
</style>