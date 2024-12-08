package com.example.adivinar

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.content.Intent
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import kotlin.random.Random

class MainActivity : AppCompatActivity() {

    private lateinit var textViewMessage: TextView
    private lateinit var editTextGuess: EditText
    private lateinit var buttonGuess: Button
    private lateinit var textViewAttempts: TextView
    private lateinit var buttonRestart: Button

    private var randomNumber = 0
    private var attemptsRemaining = 10

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Inicializar elementos de la UI
        textViewMessage = findViewById(R.id.textViewMessage)
        editTextGuess = findViewById(R.id.editTextGuess)
        buttonGuess = findViewById(R.id.buttonGuess)
        textViewAttempts = findViewById(R.id.textViewAttempts)
        buttonRestart = findViewById(R.id.buttonRestart)

        // Iniciar un nuevo juego
        startGame()

        buttonGuess.setOnClickListener {
            makeGuess()
        }

        buttonRestart.setOnClickListener {
            startGame()
        }
    }

    private fun startGame() {
        randomNumber = Random.nextInt(1, 101)
        attemptsRemaining = 10
        textViewMessage.text = "Estoy pensando en un número entre 1 y 100."
        textViewAttempts.text = "Intentos restantes: $attemptsRemaining"
        editTextGuess.text?.clear()
        enableInput()
    }

    private fun makeGuess() {
        val userGuess = editTextGuess.text.toString().trim().toIntOrNull()

        if (userGuess != null) {
            // Validar que el número tenga máximo 3 dígitos
            if (userGuess < 1 || userGuess > 100) {
                textViewMessage.text = "Por favor, ingresa un número entre 1 y 100."
                return
            }

            attemptsRemaining--
            textViewAttempts.text = "Intentos restantes: $attemptsRemaining"

            when {
                userGuess < randomNumber -> {
                    textViewMessage.text = "¡Demasiado bajo! Intenta de nuevo."
                }
                userGuess > randomNumber -> {
                    textViewMessage.text = "¡Demasiado alto! Intenta de nuevo."
                }
                else -> {
                    textViewMessage.text = "¡Felicidades! ¡Adivinaste el número!"
                    disableInput()
                }
            }

            if (attemptsRemaining == 0 && userGuess != randomNumber) {
                textViewMessage.text = "¡Perdiste! El número era $randomNumber."
                disableInput()
            }
        } else {
            textViewMessage.text = "Por favor, ingresa un número válido."
        }
    }

    private fun disableInput() {
        buttonGuess.isEnabled = false
        editTextGuess.isEnabled = false
    }

    private fun enableInput() {
        buttonGuess.isEnabled = true
        editTextGuess.isEnabled = true
    }
}

class SplashScreenActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.splash_screen)

        Handler(Looper.getMainLooper()).postDelayed({
            startActivity(Intent(this, MainActivity::class.java))
            finish()
        }, 3000)
    }
}
