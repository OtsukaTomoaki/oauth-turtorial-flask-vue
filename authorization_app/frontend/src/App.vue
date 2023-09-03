<template>
  <div>
    <h2>Login</h2>
    <input v-model="username" placeholder="Username" />
    <input type="password" v-model="password" placeholder="Password" />
    <button @click="login">Login</button>
    <p>{{ message }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      message: '',
    };
  },
  methods: {
    async login() {
      try {
        const response = await fetch('http://localhost:6001/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password,
          }),
        });
        const data = await response.json();
        this.message = data.message;
      } catch (error) {
        this.message = 'An error occurred.';
      }
    },
  },
};
</script>
