from flask import Flask, request, jsonify

app = Flask(__name__, template_folder=".")
app.config['ALLOWED_METHODS'] = ['GET','POST','DELETE','PUT']


data = []
# 데이터는 data[] 에 저장한다. Request는 Postman 웹 api 테스터에서 전송한다.

# POST에 써야하는 JSON 데이터 예시 복붙용 !!
'''
# EVENT
{
    "event_id" : "test",
    "title" : "",
    "description" : "",
    "start_time" : "",
    "end_time" : "",
    "total_winners" : "",
    "rewards" : "",
    "created_by" : "",
    "missions": [
        {
        "title" : "",
        "type" : "kakao",
        "url" : "",
        "point" : ""
        },
        {
        "title" : "",
        "type" : "instagram",
        "url" : "",
        "point" : ""
        }
    ],
    
}

# USER
{
    "user_id" : "user1",
    "name" : "",
    "email" : "",
    "user_type" : "Google",
    "created_at" : ""
}

# Mission
{
    "mission_id" : "",
    "event_id" : "",
    "title" : "",
    "description : ""
}

# EVENT USER
{
    "event_id" : "",
    "user_id" : "",
    "Points_Earned" : "",
    "Share_Link" : ""
}
'''

########################## EVENT CRUD #############################   
# POST event : request로 event 생성
@app.route("/api/event",methods=["POST"])
def create_event():
    try:
        request_data = request.get_json() #요청으로 들어온 json을 저장(생성할 이벤트 데이터)
        print(request_data)
        data.append(request_data) #이벤트 데이터를 목록(data[])에 추가
        return jsonify({"message":"event created successfully"}), 200
    except Exception as e:
        return jsonify({"message":"event creation failed"})

# GET events : 전체 event 조회
@app.route("/api/events", methods=["GET"])
def get_events():
    event_data=[]
    try:
        for element in data: # data[] 에서 event 데이터만 추출,저장 --> 알고리즘 개선 고민하기!!!!!!!!!!!
            if 'event_id' in element:
                event_data.append(element)
        return jsonify(event_data), 200 # 데이터 리스트(이벤트들) 반환
    except Exception as e:
        return jsonify({"message":"get events failed"})
    
# GET event : 특정 event 조회 by event_id
@app.route("/api/event/<event_id>", methods=["GET"])
def get_event(event_id):
    for event in data:
        if 'event_id' in event and event['event_id'] == event_id:
            return jsonify(event),200
    return jsonify({"message":"event not found"}), 404

# PUT event : request로 특정 event 수정 (uri로 event_id를 표시하고 request data에 정보를 보내야한다.)
@app.route("/api/event/<event_id>", methods=["PUT"])
def update_event(event_id):
    update_data = request.json #업데이트할 데이터 저장
    for i, event in enumerate(data):
        if 'event_id' in event and event["event_id"] == event_id:
            data[i] = update_data
            return jsonify({"message":"event updated successfully"}),200
    return jsonify({"message":"event not found"},
                   update_data ),404

# DELETE event : 특정 event 삭제 by event_id
@app.route("/api/event/<event_id>",methods=["DELETE"])
def delete_event(event_id):
    if request.method == "DELETE":
        for event in data:
            if 'event_id' in event and event['event_id'] == event_id:
                data.remove(event)
                return jsonify({"message":"event deleted successfully"}),200
    return jsonify({"message":"event not found"}),404    
            
            
            
########################## USER CRUD #############################   
# POST user : request로 user 생성
@app.route("/api/user",methods=["POST"])
def create_user():
    try:
        request_data = request.get_json() #요청으로 들어온 json을 저장(생성할 유저 데이터)
        print(request_data)
        data.append(request_data) #유저 데이터를 목록(data[])에 추가
        return jsonify({"message":"user created successfully"}), 200
    except Exception as e:
        return jsonify({"message":"user creation failed"}),500

# GET users : 전체 user 조회
@app.route("/api/users", methods=["GET"])
def get_users():
    try:
        user_data=[]
        for element in data: # data[] 에서 user 데이터만 추출,저장 --> 알고리즘 개선 고민하기!!!!!!!!!!!
            if 'user_id' in element:
                user_data.append(element)
        return jsonify(user_data), 200 # 데이터 리스트(유저들) 반환
    except Exception as e:
        return jsonify({"message" : "get users data failed"}),500
    
# GET user : 특정 user 조회 by user_id
@app.route("/api/user/<user_id>", methods=["GET"])
def get_user(user_id):
    for user in data:
        if 'user_id' in user and user['user_id'] == user_id:
            return jsonify(user),200
    return jsonify({"message":"user not found"}), 404

# PUT user : request로 특정 user 수정
@app.route("/api/user/<user_id>", methods=["PUT"])
def update_user(user_id):
    update_data = request.json #업데이트할 데이터 저장
    for i, user in enumerate(data):
        if 'user_id' in user and user["user_id"] == user_id:
            data[i] = update_data
            return jsonify({"message":"user updated successfully"}),200
    return jsonify({"message":"user not found"},
                   update_data ),404

# DELETE user : 특정 user 삭제 by user_id
@app.route("/api/user/<user_id>",methods=["DELETE"])
def delete_user(user_id):
    if request.method == "DELETE":
        for user in data:
            if 'user_id' in user and user['user_id'] == user_id:
                data.remove(user)
                return jsonify({"message":"user deleted successfully"}),200
    return jsonify({"message":"user not found"}),404    
            

    
# run
if __name__ == "__main__":
    app.run(host="localhost",port=8080,debug=False)
