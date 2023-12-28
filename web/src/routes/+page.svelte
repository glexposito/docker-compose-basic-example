<script lang="ts">
    import { onMount } from 'svelte';
  
    let colors: string[];
  
    onMount(async () => {
      const response = await fetch('http://0.0.0.0:8000/colors');
      colors = await response.json();
    });
</script>

<h1>Welcome to Svelte App!</h1>
<h2>Show colors from API response!</h2>
<h3>{colors}</h3>
