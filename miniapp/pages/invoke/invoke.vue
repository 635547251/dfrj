<template>
	<view class="chat-container">
		<view class="messages">
			<view class="message" v-for="message in messages" :key="message.id">
				<view class="message-content" :class="{ 'mine': message.isMine }">
					{{ message.text }}
				</view>
			</view>
		</view>
		<view class="input-container">
			<button @click="sendMessage">发送</button>
			<input v-model="newMessage" @click="sendMessage" placeholder="输入消息" />
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				messages: [{
						id: 1,
						text: '你好！1233333333333333333333333333333333333333333333333333',
						isMine: false
					},
					{
						id: 2,
						text: '嗨，你好！',
						isMine: true
					},
					{
						id: 3,
						text: '嗨，你好！',
						isMine: false
					},
					{
						id: 4,
						text: '嗨，你好！',
						isMine: true
					},
					{
						id: 1,
						text: '你好！',
						isMine: false
					},
					{
						id: 2,
						text: '嗨，你好！',
						isMine: true
					},
					{
						id: 3,
						text: '嗨，你好！',
						isMine: false
					},
					{
						id: 4,
						text: '嗨，你好！',
						isMine: true
					},
					{
						id: 1,
						text: '你好！',
						isMine: false
					},
					{
						id: 2,
						text: '嗨，你好！',
						isMine: true
					},
					{
						id: 3,
						text: '嗨，你好！',
						isMine: false
					},
					{
						id: 4,
						text: '嗨，你好！',
						isMine: true
					},
					{
						id: 1,
						text: '你好！',
						isMine: false
					},
					{
						id: 2,
						text: '嗨，你好！',
						isMine: true
					},
					{
						id: 3,
						text: '嗨，你好！',
						isMine: false
					},
					{
						id: 4,
						text: '嗨，你好！',
						isMine: true
					},
					{
						id: 1,
						text: '你好！',
						isMine: false
					},
					{
						id: 2,
						text: '嗨，你好！',
						isMine: true
					},
					{
						id: 3,
						text: '嗨，你好！',
						isMine: false
					},
					{
						id: 4,
						text: '嗨，你好！',
						isMine: true
					},
					{
						id: 1,
						text: '你好！',
						isMine: false
					},
					{
						id: 2,
						text: '嗨，你好！',
						isMine: true
					},
					{
						id: 3,
						text: '嗨，你好！',
						isMine: false
					},
					{
						id: 4,
						text: '嗨，你好！',
						isMine: true
					},
					{
						id: 1,
						text: '你好！',
						isMine: false
					},
					{
						id: 2,
						text: '嗨，你好！',
						isMine: true
					},
					{
						id: 3,
						text: '嗨，你好！',
						isMine: false
					},
					{
						id: 4,
						text: '嗨，你好！',
						isMine: true
					},
					{
						id: 1,
						text: '你好！',
						isMine: false
					},
					{
						id: 2,
						text: '嗨，你好！',
						isMine: true
					},
					{
						id: 3,
						text: '嗨，你好！',
						isMine: false
					},
					{
						id: 4,
						text: '嗨，你好！',
						isMine: true
					},

					{
						id: 1,
						text: '你好！',
						isMine: false
					},
					{
						id: 2,
						text: '嗨，你好！',
						isMine: true
					},
					{
						id: 3,
						text: '嗨，你好！',
						isMine: false
					},
					{
						id: 4,
						text: '嗨，你好！',
						isMine: true
					},
					{
						id: 1,
						text: '你好！',
						isMine: false
					},
					{
						id: 2,
						text: '嗨，你好！',
						isMine: true
					},
					{
						id: 3,
						text: '嗨，你好！',
						isMine: false
					},
					{
						id: 4,
						text: '嗨，你好！',
						isMine: true
					},
					{
						id: 1,
						text: '你好！',
						isMine: false
					},
					{
						id: 2,
						text: '嗨，你好！',
						isMine: true
					},
					{
						id: 3,
						text: '嗨，你好！',
						isMine: false
					},
					{
						id: 4,
						text: '嗨，你好！',
						isMine: true
					},
					{
						id: 1,
						text: '你好！',
						isMine: false
					},
					{
						id: 2,
						text: '嗨，你好！',
						isMine: true
					},
					{
						id: 3,
						text: '嗨，你好！',
						isMine: false
					},
					{
						id: 4,
						text: '嗨，你好！',
						isMine: true
					},

				],
				newMessage: ''
			}
		},
		methods: {
			sendMessage: function() {
				if (this.newMessage.trim()) {
					const id = this.messages.length + 1;
					this.messages.push({
						id,
						text: this.newMessage,
						isMine: true
					});
					this.newMessage = ''; // 清空输入框
				}
			},
		}
	}
</script>

<style>
	.chat-container {
		display: flex;
		flex-direction: column;
		height: 100vh;
		border: 1px solid #ccc;
		background-color: #0f131b;
	}

	.messages {
		flex: 1;
		overflow-y: auto;
		padding: 10px;
		display: flex;
		flex-direction: column;
	}

	.message {
		margin-bottom: 10px;
	}

	.message-content {
		display: inline-block;
		padding: 5px 10px;
		border-radius: 10px;
		background-color: #5659cf;
		color: white;
		word-break: break-all;
		word-wrap: break-word;
	}

	.message-content.mine {
		float: right;
		background-color: #32346f;
	}

	.input-container {
		display: flex;
		padding: 10px;
		background-color: #151728;
	}

	.input-container input {
		flex: 1;
		margin-right: 10px;
		padding: 5px;
		background-color: #0f131b;
	}

	.input-container button {
		padding: 5px 10px;
		background-color: #17abb4;
		color: white;
	}
</style>