export type ChatRole = "user" | "assistant" | "system";

export interface ChatRequestContract {
  sessionId: string;
  message: string;
}

export interface ChatMessageContract {
  id: string;
  role: ChatRole;
  content: string;
}

export interface ChatResponseContract {
  sessionId: string;
  reply: ChatMessageContract;
  flowState: string;
}
