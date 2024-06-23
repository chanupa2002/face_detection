import cv2
import face_recognition

known_face_encodings = []
known_face_names = []

kp1_img = face_recognition.load_image_file(r"C:\Users\athsa\OneDrive\Desktop\Programming\Python\refer.png")
kp2_img = face_recognition.load_image_file(r"C:\Users\athsa\OneDrive\Desktop\Programming\Python\sha.jpeg")
kp3_img = face_recognition.load_image_file(r"C:\Users\athsa\OneDrive\Desktop\Programming\Python\sal.jpeg")

kp1_encoding = face_recognition.face_encodings(kp1_img)[0]
kp2_encoding = face_recognition.face_encodings(kp2_img)[0]
kp3_encoding = face_recognition.face_encodings(kp3_img)[0]

known_face_encodings.append(kp1_encoding)
known_face_encodings.append(kp2_encoding)
known_face_encodings.append(kp3_encoding)

known_face_names.append("Chanupa Athsara")
known_face_names.append("Sharuk Khan")
known_face_names.append("Salman Khan")

p1 = 0
p2 = 0
p3 = 0

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    face_location = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_location)

    for (top, right, bottom, left), face_encoding in zip(face_location, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

            if(name == "Chanupa Athsara"):
                p1 = 1

            if(name == "Sharuk Khan"):
                p2 = 1

            if(name == "Salman Khan"):
                p3 = 1

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)


    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

print("\nSharuk Khan : " + str(p2))
print("\nChanupa Athsara : " + str(p1))
print("\nSalman Khan : " + str(p3))
