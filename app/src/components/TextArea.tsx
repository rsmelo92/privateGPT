import { SendTwoTone } from "@mui/icons-material";
import { Box, IconButton, TextField } from "@mui/material";
import { useState } from "react";

type TextAreaProps = {
  onSend?: (value: string) => void;
};

export const TextArea = ({ onSend: _onSend }: TextAreaProps) => {
  const [message, setMessage] = useState("");
  const onSend = async () => {
    if (message === "") return;
    _onSend(message);
    setMessage("");
  };
  return (
    <Box
      component="form"
      noValidate
      autoComplete="off"
      sx={{
        width: "100%",
        alignSelf: "flex-end",
        position: "relative",
      }}
    >
      <TextField
        autoFocus
        fullWidth
        multiline
        color="primary"
        rows={4}
        placeholder="Type a message here"
        value={message}
        onChange={(e) => {
          setMessage(e.target.value);
        }}
        onKeyPress={(e) => {
          if (e.key === "Enter") {
            e.preventDefault();
            onSend();
          }
        }}
      />
      <Box
        sx={{
          width: "100%",
          display: "flex",
          position: "absolute",
          right: 0,
          left: 0,
          bottom: 0,
          justifyContent: "flex-end",
          padding: "4px 8px",
        }}
      >
        <IconButton aria-label="delete" onClick={onSend}>
          <SendTwoTone />
        </IconButton>
      </Box>
    </Box>
  );
};
