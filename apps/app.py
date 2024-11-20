from flask import Flask, render_template, send_from_directory
# from pywebpush import webpush, WebPushException

app = Flask(__name__)
subscriptions = [] # 通知の受取口
VAPID_PRIVATE_KEY = 'XjKtnq35riGHMyrrGTGCPTsFKrUWv6kVJzXfzjCbt8o'
VAPID_PUBLIC_KEY  = ''

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sw.js')
def serve_sw():
    return send_from_directory('static', 'sw.js')

# @app.route('/subscribe', methods=['POST'])
# def subscribe():
#     subscription = request.json
#     subscriptions.append(subscription)
#     return jsonify({'status': 'success'}), 201


@app.route('/send_push', methods=['POST'])
def send_push():
    message = {
        "title": "Hello!",
        "body": "This is a push notification"
    }

    for subscription in subscriptions:
        try:
            webpush(
                subscription_info=subscription,
                data=json.dumps(message),
                vapid_private_key=VAPID_PRIVATE_KEY,
                vapid_claims={
                    "sub": "mailto:you@example.com"
                }
            )
        except WebPushException as ex:
            print("Webプッシュ通知に失敗しました: {}", repr(ex))
    
    return jsonify({'status': 'push sent'})

if __name__ == "__main__":
    app.run(debug=True, port=443, ssl_context=('cert.pem', 'key.pem'), host='0.0.0.0')