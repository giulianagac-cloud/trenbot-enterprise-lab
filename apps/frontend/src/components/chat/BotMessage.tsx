import styles from "./MessageBubble.module.css";

export function BotMessage({ content }: { content: string }) {
  return (
    <div className={`${styles.row} ${styles.rowAssistant}`}>
      <div>
        <div className={styles.label}>Assistant</div>
        <div className={`${styles.bubble} ${styles.bubbleAssistant}`}>{content}</div>
      </div>
    </div>
  );
}

