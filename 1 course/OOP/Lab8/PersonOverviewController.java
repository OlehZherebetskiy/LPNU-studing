package ch.makery.address.view;

import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Label;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import ch.makery.address.Mainapp;
import ch.makery.address.model.Domain;
import ch.makery.address.util.DateUtil;

public class PersonOverviewController {
    @FXML
    private TableView<Domain> personTable;
    @FXML
    private TableColumn<Domain, String> NumberColumn;
    @FXML
    private TableColumn<Domain, String> NameColumn;
    private int i;
    @FXML
    private Label NameLabel;
    @FXML
    private Label UnitLabel;
    @FXML
    private Label NumberLabel;
    @FXML
    private Label Unit_priceLabel;
    @FXML
    private Label Receipt_dLabel;
    @FXML
    private Label AboutLabel;

    // Ссылка на главное приложение.
    private Mainapp mainApp;

    /**
     * Конструктор.
     * Конструктор вызывается раньше метода initialize().
     */
    public PersonOverviewController() {
    }

    /**
     * Инициализация класса-контроллера. Этот метод вызывается автоматически
     * после того, как fxml-файл будет загружен.
     */
    @FXML
    private void initialize() {
        // Инициализация таблицы адресатов с двумя столбцами.
    	//NumberColumn.setCellValueFactory(cellData -> cellData.getValue().);
    	NameColumn.setCellValueFactory(cellData -> cellData.getValue().getpName());
    	NumberColumn.setCellValueFactory(cellData -> cellData.getValue().getpNumber());
    	
    	showDomainDetails(null);
    	
    	 personTable.getSelectionModel().selectedItemProperty().addListener(
    	            (observable, oldValue, newValue) -> showDomainDetails(newValue));
    
    
    
    }

    /**
     * Вызывается главным приложением, которое даёт на себя ссылку.
     * 
     * @param mainApp
     */
    public void setMainApp(Mainapp mainApp) {
        this.mainApp = mainApp;

        // Добавление в таблицу данных из наблюдаемого списка
        personTable.setItems(mainApp.getPersonData());
    }
    
    private void showDomainDetails(Domain dom) {
        if (dom != null) {
            // Заполняем метки информацией из объекта person.
            NameLabel.setText(dom.getName());
            NumberLabel.setText(dom.getNumber());
            UnitLabel.setText(dom.getUnit());
            Unit_priceLabel.setText(dom.getUnit_price());
            Receipt_dLabel.setText(dom.getReceipt_d());
            AboutLabel.setText(dom.getAbout().toString());

            // TODO: Нам нужен способ для перевода дня рождения в тип String! 
            //Receipt_dLabel.setText(DateUtil.format(dom.getReceipt_d()));
        } else {
            // Если Person = null, то убираем весь текст.
            NameLabel.setText("");
            NameLabel.setText("");
            UnitLabel.setText("");
            Unit_priceLabel.setText("");
            Receipt_dLabel.setText("");
            AboutLabel.setText("");
        }
    }
    
    
    @FXML
	private void handleDeletePerson() {
    	 int selectedIndex = personTable.getSelectionModel().getSelectedIndex();
    	    if (selectedIndex >= 0) {
    	        personTable.getItems().remove(selectedIndex);
    	    } else {
    	        // Ничего не выбрано.
    	        Alert alert = new Alert(AlertType.WARNING);
    	        alert.initOwner(mainApp.getPrimaryStage());
    	        alert.setTitle("No Selection");
    	        alert.setHeaderText("No Person Selected");
    	        alert.setContentText("Please select a person in the table.");

    	        alert.showAndWait();
    	    }
    }
    @FXML
    private void handleSortPerson() {
    
    	List<Domain> a = new ArrayList<Domain>();
    	for(int i=0; i<personTable.getItems().size()-1;i++)
    	{
    		a.add(personTable.getItems().get(i));
    		
    	}
    	
    		
    		personTable.getItems().clear();
    	a.sort(null);
    	for(int i=0; i<a.size();i++)
    	{
    		
    		personTable.getItems().add(a.get(i));
    	}
    	
    		
    		a.clear();
    	
    	
    	
    }
    @FXML
    private void handleClearPerson() {
    	personTable.getItems().clear();
    }
    
    
    
    @FXML
    private void handleNewPerson() throws IOException {
        Domain tempPerson = new Domain();
        boolean okClicked = mainApp.showPersonEditDialog(tempPerson);
        if (okClicked) {
            mainApp.getPersonData().add(tempPerson);
        }
    }

    /**
     * Вызывается, когда пользователь кликает по кнопка Edit...
     * Открывает диалоговое окно для изменения выбранного адресата.
     */
    @FXML
    private void handleEditPerson() {
    	Domain selectedPerson = personTable.getSelectionModel().getSelectedItem();
        if (selectedPerson != null) {
            boolean okClicked = mainApp.showPersonEditDialog(selectedPerson);
            if (okClicked) {
                showDomainDetails(selectedPerson);
            }
            personTable.getSelectionModel().getSelectedIndex();
           
        } else {
            // Ничего не выбрано.
            Alert alert = new Alert(AlertType.WARNING);
            alert.initOwner(mainApp.getPrimaryStage());
            alert.setTitle("No Selection");
            alert.setHeaderText("No Person Selected");
            alert.setContentText("Please select a person in the table.");

            alert.showAndWait();
        }
    }
   
    
}