import { Box, LinearProgress } from "@mui/material";
import { useState } from "react";

import { TextArea } from "./TextArea";

const fetchAnswer = (
  text: string,
  onAnswer: (res: string) => void,
  onFinally: () => void,
) => {
  fetch(`http://localhost:8000/ask?query=${text}`)
    .then((res) => res.text())
    .then((res) => {
      onAnswer(res);
    })
    .catch(console.error)
    .finally(() => {
      onFinally();
    });
};

export const Main = () => {
  const [textContent, setTextContent] = useState([
    "First questions take longer than others",
    "Hello World!"
  ]);

  const [isLoading, setIsLoading] = useState(false);

  const onSend = (text: string) => {
    setTextContent([text, ...textContent]);
    setIsLoading(true);
    fetchAnswer(
      text,
      (res) => {
        setTextContent([res, text, ...textContent]);
      },
      () => {
        setIsLoading(false);
      },
    );
  };

  return (
    <Box
      sx={{
        display: "flex",
        flexWrap: "wrap",
        justifyContent: "space-between",
        height: "100vh",
        padding: "24px",
        position: "relative",
      }}
    >
      {isLoading && (
        <Box
          sx={{
            width: "100%",
            position: "absolute",
            top: 0,
            left: 0,
            right: 0,
          }}
        >
          <LinearProgress color="inherit" />
        </Box>
      )}
      <Box
        sx={{
          overflow: "scroll",
          height: "75%",
          width: "100%",
          display: "flex",
          flexDirection: "column-reverse",
        }}
      >
        {textContent.map((t, idx) => (
          <p key={idx}>{t}</p>
        ))}
      </Box>

      <TextArea onSend={onSend} />
    </Box>
  );
};
