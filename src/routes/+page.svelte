<script>
	import Inputd from './inputd.svelte';
	import { createEventDispatcher } from 'svelte';

	import {onMount} from 'svelte';


	
	function myEventHandler(e) {
       console.log('--??--',e.detail.myName)
	  
	   try {
		e.detail.myName.focus()
	    e.detail.myName.showPicker()
    } catch (err) {
      console.log(err)
    }



  }


</script>

<p>
	<button on:click={func}>Show Picker</button>
</p>

<div on:mouseover={func} style="padding:20px;background:silver">
	<p>
		<Inputd on:myEvent={myEventHandler} />

		<!-- <input id='dtp' class="datepicker1" on:mousemove={func} bind:this={inputEl} type='datetime-local' /> -->
	</p>
</div>

<p>
	<a href=" https://github.com/gitpod-samples/template-sveltekit/tree/main">Template </a>
</p>

<style>
	.datepicker {
		position: relative;
		cursor: pointer;
		box-sizing: border-box;
		line-height: normal !important;
	}
	.datepicker::-webkit-calendar-picker-indicator {
		position: absolute;
		right: 0;
		width: 100%;
		height: 100%;
		margin: 0;
		padding: 0;
		opacity: 0;
		cursor: pointer;
	}
</style>
