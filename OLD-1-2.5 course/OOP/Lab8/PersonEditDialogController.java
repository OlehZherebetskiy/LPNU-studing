package ch.makery.address.view;


import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.Label;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import ch.makery.address.model.Domain;
import ch.makery.address.util.DateUtil;

/**
 * Окно для изменения информации об адресате.
 * 
 * @author Marco Jakob
 */
public class PersonEditDialogController {

    @FXML
    private TextField NameLabel  ;
    @FXML
    private TextField UnitLabel ;
    @FXML
    private TextField NumberLabel ;
    @FXML
    private TextField Unit_priceLabel ;
    @FXML
    private TextField Receipt_dLabel ;
    @FXML
    private TextField AboutLabel ;


    private Stage dialogStage;
    private Domain person;
    private boolean okClicked = false;

    /**
     * Инициализирует класс-контроллер. Этот метод вызывается автоматически
     * после того, как fxml-файл будет загружен.
     */
    @FXML
    private void initialize() {
    }

    /**
     * Устанавливает сцену для этого окна.
     * 
     * @param dialogStage
     */
    public void setDialogStage(Stage dialogStage) {
        this.dialogStage = dialogStage;
    }

    /**
     * Задаёт адресата, информацию о котором будем менять.
     * 
     * @param person
     */
    public void setPerson(Domain dom) {
        this.person = dom;
        
        	NameLabel.setText(dom.getName());
        	
        	NumberLabel.setText(dom.getNumber());
        	
        	UnitLabel.setText(dom.getUnit());
        	
        	Unit_priceLabel.setText(dom.getUnit_price());
        	
        	Receipt_dLabel.setText(dom.getReceipt_d());
        	
        	AboutLabel.setText(dom.getAbout().toString());
            
        
        Receipt_dLabel.setPromptText("dd.mm.yyyy");
    }

    /**
     * Returns true, если пользователь кликнул OK, в другом случае false.
     * 
     * @return
     */
    public boolean isOkClicked() {
        return okClicked;
    }

    /**
     * Вызывается, когда пользователь кликнул по кнопке OK.
     */
    @FXML
    private void handleOk() {
        if (isInputValid()) {
            person.setName(NameLabel.getText());
            person.setUnit(UnitLabel.getText());
            person.setNumbers(NumberLabel.getText());
            person.setUnit_price(Unit_priceLabel.getText());
            person.setReceipt_d(Receipt_dLabel.getText());
            //person.setBirthday(DateUtil.parse(AboutLabel.getText()));
            

            okClicked = true;
            dialogStage.close();
        }
    }

    /**
     * Вызывается, когда пользователь кликнул по кнопке Cancel.
     */
    @FXML
    private void handleCancel() {
        dialogStage.close();
    }

    /**
     * Проверяет пользовательский ввод в текстовых полях.
     * 
     * @return true, если пользовательский ввод корректен
     */ 
    private boolean isInputValid() {
        String errorMessage = "";

        if (NameLabel.getText() == null || NameLabel.getText().length() == 0) {
            errorMessage += "No valid  Name!\n"; 
        }
        if (UnitLabel.getText() == null || UnitLabel.getText().length() == 0) {
            errorMessage += "No valid Unit !\n"; 
        }
        if (NumberLabel.getText() == null || NumberLabel.getText().length() == 0) {
            errorMessage += "No valid Number!\n"; 
        }

        if (Unit_priceLabel.getText() == null || Unit_priceLabel.getText().length() == 0) {
            errorMessage += "No valid Unit price !\n"; 
        } 
        

        if (Receipt_dLabel.getText() == null || Receipt_dLabel.getText().length() == 0) {
            errorMessage += "No valid Receipt date!\n"; 
        }

        if (errorMessage.length() == 0) {
            return true;
        } else {
            // Показываем сообщение об ошибке.
            Alert alert = new Alert(AlertType.ERROR);
            alert.initOwner(dialogStage);
            alert.setTitle("Invalid Fields");
            alert.setHeaderText("Please correct invalid fields");
            alert.setContentText(errorMessage);
            
            alert.showAndWait();
            
            return false;
        }
    }}