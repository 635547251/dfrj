<template>
	<view class='content'>
		<image class="background" src="/static/bg.webp" mode="aspectFill"></image>
		<button class="image-button" @click="handleClick">开始占卜</button>
	</view>
</template>

<script>
	export default {
		data() {
			return {}
		},
		onLoad() {

		},
		methods: {
			handleClick: function() {
				uni.navigateTo({
					url: '/pages/invoke/invoke'
				});
			}
		}
	}
</script>

<style>
	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}

	.background {
		height: 100vh;
		width: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.image-button {
		background-color: #ffd35c;
		color: black;
		width: 80%;
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
	}
</style>