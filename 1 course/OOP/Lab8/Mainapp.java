package ch.makery.address;


import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.BorderPane;
import javafx.stage.Modality;
import javafx.stage.Stage;
import ch.makery.address.model.Domain;
import ch.makery.address.view.PersonEditDialogController;
import ch.makery.address.view.PersonOverviewController;
import ch.makery.address.File_work;
import ch.makery.address.Menu;



public class Mainapp extends Application {

    private static boolean point;
	private static Stage primaryStage;
    private BorderPane rootLayout;
    /**
     * ������, � ���� ������������ ������ ���������.
     */
    private ObservableList<Domain> personData = FXCollections.observableArrayList();

    /**
     * �����������
     */
    public Mainapp() {
        // � �������� ������� ��������� ��������� ������
        for(int i=0;i<20;i++)
        {
        	personData.add(new Domain("rand"));
        }
       
    }
  
    /**
     * ���������� ������ � ���� ������������ ������ ���������.
     * @return
     */
    public ObservableList<Domain> getPersonData() {
        return personData;
    }
    @Override
    public void start(Stage primaryStage) {
        this.primaryStage = primaryStage;
        this.primaryStage.setTitle("AddressApp");

        initRootLayout();

        showPersonOverview();
    }

    /**
     * �������������� �������� �����.
     */
    public void initRootLayout() {
        try {
            // ��������� �������� ����� �� fxml �����.
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(Mainapp.class.getResource("view/RootLayout.fxml"));
            rootLayout = (BorderPane) loader.load();

            // ���������� �����, ���������� �������� �����.
            Scene scene = new Scene(rootLayout);
            primaryStage.setScene(scene);
            primaryStage.show();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * ���������� � �������� ������ �������� �� ���������.
     */
    public void showPersonOverview() {
        try {
            // ��������� �������� �� ���������.
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(Mainapp.class.getResource("view/PersonOverview.fxml"));
            AnchorPane personOverview = (AnchorPane) loader.load();

            // �������� �������� �� ��������� � ����� ��������� ������.
            rootLayout.setCenter(personOverview);
         // ��� ����������� ������ � �������� ����������.
            PersonOverviewController controller = loader.getController();
            controller.setMainApp(this);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * ���������� ������� �����.
     * @return
     */
    public static Stage getPrimaryStage() {
        return primaryStage;
    }

    public static void main(String[] args) throws IOException {
        launch(args);
        
        List<Domain> con = new ArrayList<Domain>();
		
		
		File_work<Domain> File_work = new File_work<Domain>();
		//if (args.length > 0)  point = Menu.prehelp(args[0]) ;
		Menu.help();
		Scanner sc = new Scanner(System.in);
		Domain element = new Domain();
    }

	public boolean showPersonEditDialog(Domain tempPerson) {
		try {
	        // ��������� fxml-���� � ������ ����� �����
	        // ��� ������������ ����������� ����.
	        FXMLLoader loader = new FXMLLoader();
	        loader.setLocation(Mainapp.class.getResource("view/PersonEditDialog.fxml"));
	        AnchorPane page = (AnchorPane) loader.load();

	        // ������ ���������� ���� Stage.
	        Stage dialogStage = new Stage();
	        dialogStage.setTitle("Edit Person");
	        dialogStage.initModality(Modality.WINDOW_MODAL);
	        dialogStage.initOwner(primaryStage);
	        Scene scene = new Scene(page);
	        dialogStage.setScene(scene);

	        // ������� �������� � ����������.
	        PersonEditDialogController controller = loader.getController();
	        controller.setDialogStage(dialogStage);
	        controller.setPerson(tempPerson);

	        // ���������� ���������� ���� � ���, ���� ������������ ��� �� �������
	        dialogStage.showAndWait();

	        return controller.isOkClicked();
	    } catch (IOException e) {
	        e.printStackTrace();
	        return false;
	    }
	}
	
	
    
    
}