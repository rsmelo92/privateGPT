import { SendTwoTone } from "@mui/icons-material";
import { Box, IconButton, TextField } from "@mui/material";
import React from "react";

export const TextArea = () => {
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
        <IconButton aria-label="delete">
          <SendTwoTone />
        </IconButton>
      </Box>
    </Box>
  );
};
