public class MediatorPatternTest {
    public static void main(String[] args) {
        ChatRoom chatRoom = new ChatRoom();
        
        User john = new UserImpl(chatRoom, "John");
        User jane = new UserImpl(chatRoom, "Jane");
        
        chatRoom.addUser(john);
        chatRoom.addUser(jane);

        john.send("Hello Jane");
        jane.send("Hey John");
    }
}
