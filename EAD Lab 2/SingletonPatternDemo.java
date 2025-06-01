class SingletonLogger {
    private static SingletonLogger instance;

    private SingletonLogger() {
        System.out.println("Logger Initialized.");
    }

    public static SingletonLogger getInstance() {
        if (instance == null) {
            instance = new SingletonLogger();
        }
        return instance;
    }

    public void log(String message) {
        System.out.println("Log: " + message);
    }
}

public class SingletonPatternDemo {
    public static void main(String[] args) {
        SingletonLogger logger1 = SingletonLogger.getInstance();
        logger1.log("First message");

        SingletonLogger logger2 = SingletonLogger.getInstance();
        logger2.log("Second message");

        System.out.println("Are both instances same? " + (logger1 == logger2));
    }
}
